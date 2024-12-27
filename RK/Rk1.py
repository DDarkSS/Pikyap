class CD:

    def __init__(self, cd_id, title, artist, genre, library_id):
        self.cd_id = cd_id
        self.title = title
        self.artist = artist
        self.genre = genre
        self.library_id = library_id

class Library:

    def __init__(self, library_id, name):
        self.library_id = library_id
        self.name = name
        self.cds = []

    def add_cd(self, cd):
        self.cds.append(cd)

libraries = [
    Library(1, "Central Library"),
    Library(2, "Music Hall")
]

cds = [
    CD(1, "Thriller", "Michael Jackson", "Pop", 1),
    CD(2, "Back in Black", "AC/DC", "Rock", 1),
    CD(3, "Abbey Road", "The Beatles", "Rock", 2),
    CD(4, "Dark Side of the Moon", "Pink Floyd", "Progressive Rock", 2),
    CD(5, "Rumours", "Fleetwood Mac", "Pop Rock", 1)
]

for cd in cds:
    for library in libraries:
        if cd.library_id == library.library_id:
            library.add_cd(cd)

cd_library_list = sorted([(cd.title, library.name) for library in libraries for cd in library.cds], key=lambda x: x[0])
print("\nСписок всех связанных CD и библиотек, отсортированный по CD:")
for cd_title, library_name in cd_library_list:
    print(f"CD: {cd_title}, Библиотека: {library_name}")


library_cd_count = sorted([(library.name, len(library.cds)) for library in libraries], key=lambda x: x[1], reverse=True)
print("\nСписок библиотек с количеством CD в каждой библиотеке:")
for library_name, cd_count in library_cd_count:
    print(f"Библиотека: {library_name}, Количество CD: {cd_count}")

for cd in cds:
    cd.authors = []
cds[0].authors.extend(["Квинси Джонс", "Род Темпертон"])
cds[1].authors.extend(["Ангус Янг", "Малкольм Янг"])
cds[2].authors.extend(["Джон Леннон", "Пол Маккартни"])


authors_with_ov = [(author, cd.title, library.name)
                  for library in libraries
                  for cd in library.cds
                  for author in cd.authors
                  if author.endswith("ов")]
print("\nСписок авторов, чьи фамилии заканчиваются на 'ов', и названия их произведений:")
for author, cd_title, library_name in authors_with_ov:
    print(f"Автор: {author}, CD: {cd_title}, Библиотека: {library_name}")