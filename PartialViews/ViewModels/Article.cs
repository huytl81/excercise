using System;
using System.Collections.Generic;

namespace PartialViews.ViewModels
{
    public class Article
    {
        public string AuthorName { get; set; }

        public DateTime PublicationDate { get; set; } = DateTime.Today;

        public string Title { get; set; }

        public List<Section> Sections { get; } = new List<Section>();
    }
}
