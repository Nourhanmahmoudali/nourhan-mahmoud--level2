book_days = {}
unique_titles = set()
borrowed_books = [
    "Book A - 10",
    "Book B - 5",
    "Book C - 15",
    "Book A - 8",
    "Book B - 3",
    "Book D - 7",
]

for book_info in borrowed_books:
    title, days_str = book_info.split(" - ")
    days = int(days_str)
    book_days[title] = book_days.get(title, 0) + days

most_borrowed = max(book_days, key=book_days.get)
print("Most borrowed book:", most_borrowed)

least_borrowed = min(book_days, key=book_days.get)
print("Least borrowed book:", least_borrowed)

average_days = sum(book_days.values()) / len(book_days)
print("Average borrowing days:", average_days)

print("Unique book titles:", unique_titles)

sorted_books = sorted(book_days.items(), key=lambda x: x[1], reverse=True)
print("Books sorted by borrowing days:")
for title, days in sorted_books:
    print(f"{title}: {days} days")






