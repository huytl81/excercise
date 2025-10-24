import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListService, PagedResultDto } from '@abp/ng.core';
import { NgxDatatableModule } from '@swimlane/ngx-datatable';
import { FormGroup, FormsModule, FormBuilder, Validators } from '@angular/forms';
import { CoreModule } from '@abp/ng.core';
import { ModalComponent } from '@abp/ng.theme.shared';
import { NgbDatepickerModule, NgbDateStruct } from '@ng-bootstrap/ng-bootstrap';
import { NgbDateNativeAdapter, NgbDateAdapter } from '@ng-bootstrap/ng-bootstrap';
import { ConfirmationService, Confirmation } from '@abp/ng.theme.shared';
import { NgbDropdownModule } from '@ng-bootstrap/ng-bootstrap';
import { Authors } from '@proxy';
@Component({
  selector: 'app-author',
  standalone: true,
  imports: [CommonModule, FormsModule, NgxDatatableModule, CoreModule, ModalComponent, NgbDatepickerModule,NgbDropdownModule],
  templateUrl: './author.html',
  styleUrls: ['./author.scss'],
  providers: [ListService, { provide: NgbDateAdapter, useClass: NgbDateNativeAdapter }],
})
export class AuthorComponent implements OnInit {
  author = { items: [], totalCount: 0 } as PagedResultDto<Authors.AuthorDto>;
  isModalOpen = false;
  form: FormGroup;
  selectedAuthor = {} as Authors.AuthorDto;
  minDate: NgbDateStruct;
  maxDate: NgbDateStruct;
  constructor(
    public readonly list: ListService,
    private authorService: Authors.AuthorService,
    private fb: FormBuilder,
    private confirmation: ConfirmationService
  ) {}

  ngOnInit(): void {
    const authorStreamCreator = (query) => this.authorService.getList(query);

    this.list.hookToQuery(authorStreamCreator).subscribe((response) => {
      this.author = response;
    });

    this.minDate = { year: 1900, month: 1, day: 1 };

    // Giới hạn tối đa là hôm nay
    const today = new Date();
    this.maxDate = {
      year: today.getFullYear(),
      month: today.getMonth() + 1,
      day: today.getDate(),
    };
    
  }

  createAuthor() {
    this.selectedAuthor = {} as Authors.AuthorDto;
    this.buildForm();
    this.isModalOpen = true;
  }

  editAuthor(id: string) {
    this.authorService.get(id).subscribe(author => {
      this.selectedAuthor = author;
      this.buildForm();
      this.isModalOpen = true;
    });
  }

  deleteAuthor(id: string) {
    this.confirmation.warn('::AreYouSureToDelete', '::AreYouSure')
        .subscribe(status => {
          if (status === Confirmation.Status.confirm) {
            this.authorService.delete(id).subscribe(() => this.list.get());
          }
        });
  }

  buildForm() {
    this.form = this.fb.group({
      name: [this.selectedAuthor.name || '', Validators.required],
      birthDate: [this.selectedAuthor.birthDate ? new Date(this.selectedAuthor.birthDate) : null, Validators.required,],
      shortBio: [this.selectedAuthor.shortBio ? this.selectedAuthor.shortBio : null, Validators.required,],
    });
  }

  save() {
    if (this.form.invalid) {
      return;
    }

    if (this.selectedAuthor.id) {
      this.authorService.update(this.selectedAuthor.id, this.form.value).subscribe(() => {
          this.close();
        });
    } else {
        this.authorService.create(this.form.value).subscribe(() => {
        this.close();
      });
    }
  }
  close(){
    this.isModalOpen = false;
    this.form.reset();
    this.list.get();
  }
}

