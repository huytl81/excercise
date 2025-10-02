// filepath: book.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListService, PagedResultDto } from '@abp/ng.core';
import { Books } from '@proxy';
import { NgxDatatableModule } from '@swimlane/ngx-datatable';
import { FormsModule } from '@angular/forms';
import { CoreModule } from '@abp/ng.core';
import { ModalComponent } from '@abp/ng.theme.shared';

@Component({
  selector: 'app-book',
  standalone: true,
  imports: [CommonModule,
            FormsModule,
            NgxDatatableModule,
            CoreModule,
            ModalComponent],
  templateUrl: './book.html',
  styleUrls: ['./book.scss'],
  providers: [ListService],
})

export class BookComponent implements OnInit {
  book = { items: [], totalCount: 0 } as PagedResultDto<Books.BookDto>;
  isModalOpen = false;

  constructor(public readonly list: ListService, private bookService: Books.BookService) {}

  ngOnInit() {
    const bookStreamCreator = (query) => this.bookService.getList(query);

    this.list.hookToQuery(bookStreamCreator).subscribe((response) => {
      this.book = response;
    });
  }
  // add new method
  createBook() {
    this.isModalOpen = true;
  }
}