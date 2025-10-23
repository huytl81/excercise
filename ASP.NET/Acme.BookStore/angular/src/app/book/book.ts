// filepath: book.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormGroup, FormsModule, FormBuilder, Validators } from '@angular/forms';
import { CoreModule, ListService, PagedResultDto } from '@abp/ng.core';
import { ModalComponent, ConfirmationService, Confirmation } from '@abp/ng.theme.shared';
import { NgxDatatableModule } from '@swimlane/ngx-datatable';
import { NgbDatepickerModule, NgbDateNativeAdapter, NgbDateAdapter, NgbDropdownModule} from '@ng-bootstrap/ng-bootstrap';
import { Books } from '@proxy';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
@Component({
  selector: 'app-book',
  standalone: true,
  imports: [CommonModule, 
            FormsModule, 
            NgxDatatableModule, 
            CoreModule, 
            ModalComponent, 
            NgbDatepickerModule, 
            NgbDropdownModule],
  templateUrl: './book.html',
  styleUrls: ['./book.scss'],
  providers: [ListService, { provide: NgbDateAdapter, useClass: NgbDateNativeAdapter }],
})

export class BookComponent implements OnInit {
  book = { items: [], totalCount: 0 } as PagedResultDto<Books.BookDto>;

  selectedBook = {} as Books.BookDto;

  authors$: Observable<Books.AuthorLookupDto[]>;

  form: FormGroup;

  bookTypes = Books.bookTypeOptions;

  isModalOpen = false;

  constructor(public readonly list: ListService, 
              private bookService: Books.BookService, 
              private fb: FormBuilder, 
              private confirmation: ConfirmationService) 
  { 
    this.authors$ = bookService.getAuthorLookup().pipe(map((r) => r.items));
  }

  ngOnInit() {
    const bookStreamCreator = query => this.bookService.getList(query);

    this.list.hookToQuery(bookStreamCreator).subscribe(response => {
      this.book = response;
    });
  }

  createBook() {
    this.selectedBook = {} as Books.BookDto; // reset the selected book
    this.buildForm();
    this.isModalOpen = true;
  }

  editBook(id: string) {
    this.bookService.get(id).subscribe((book) => {
      this.selectedBook = book;
      this.buildForm();
      this.isModalOpen = true;
    });
  }

  deleteBook(id: string) {
    this.confirmation.warn('::AreYouSureToDelete', '::AreYouSure').subscribe((status) => {
      if (status === Confirmation.Status.confirm) {
        this.bookService.delete(id).subscribe(() => this.list.get());
      }
    });
  }

  buildForm() {
    this.form = this.fb.group({
      authorId: [this.selectedBook.authorId || null, Validators.required],
      name: [this.selectedBook.name || '', Validators.required],
      type: [this.selectedBook.type || null, Validators.required],
      publishDate: [this.selectedBook.publishDate ? new Date(this.selectedBook.publishDate) : null, Validators.required,],
      price: [this.selectedBook.price || null, Validators.required],
    });
  }

  save() {
    if (this.form.invalid) {
      return;
    }

    const request = this.selectedBook.id ? this.bookService.update(this.selectedBook.id, this.form.value) : this.bookService.create(this.form.value);

    request.subscribe(() => {
      this.isModalOpen = false;
      this.form.reset();
      this.list.get();
    });
  }
}
