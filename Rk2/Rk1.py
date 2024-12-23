class CD:
    def __init__(self, cd_id, title, artist, genre):
        self.cd_id = cd_id
        self.title = title
        self.artist = artist
        self.genre = genre
        self.libraries = []


class Library:
    def __init__(self, library_id, name):
        self.library_id = library_id 
        self.name = name 
        self.cds = [] 

    def add_cd(self, cd):
        self.cds.append(cd)
        cd.libraries.append(self)


cd1 = CD(cd_id=1, title="Abbey Road", artist="The Beatles", genre="Rock")
cd2 = CD(cd_id=2, title="Back in Black", artist="AC/DC", genre="Rock")
cd3 = CD(cd_id=3, title="The Dark Side of the Moon", artist="Pink Floyd", genre="Progressive Rock")
cd4 = CD(cd_id=4, title="Thriller", artist="Michael Jackson", genre="Pop")
cd5 = CD(cd_id=5, title="The Wall", artist="Pink Floyd", genre="Progressive Rock")

library1 = Library(library_id=1, name="Central Library")
library2 = Library(library_id=2, name="Community Library")

library1.add_cd(cd1)
library1.add_cd(cd2)
library1.add_cd(cd3)

library2.add_cd(cd2)
library2.add_cd(cd4)
library2.add_cd(cd5)

print("Список CD и библиотек:")
sorted_cds = sorted(cd1.libraries + cd2.libraries + cd3.libraries + cd4.libraries + cd5.libraries, key=lambda cd: cd.title)

for cd in sorted_cds:
    for library in cd.libraries:
        print(f"CD: {cd.title}, Artist: {cd.artist}, Library: {library.name}")

print("\n")

print("Список библиотек и количества CD в каждом:")
libraries_count = [(library.name, len(library.cds)) for library in [library1, library2]]
sorted_libraries = sorted(libraries_count, key=lambda x: x[1], reverse=True)

for library_name, count in sorted_libraries:
    print(f"Library: {library_name}, Number of CDs: {count}")

print("\n")

print("CD, название которых заканчивается на \"e\" и библиотеки, в которых они находятся:")
for cd in [cd1, cd2, cd3, cd4, cd5]:
    if cd.title.endswith("e"):
        for library in cd.libraries:
            print(f"CD: {cd.title}, Library: {library.name}")
