import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'perpus2.settings')

import django
django.setup()

from buku2.models import Category, Book, Pengarang


def populate():
    novel_cat = add_cat('Novel')
    joko = add_pengarang('Joko')
    budi = add_pengarang('Budi')
    ani = add_pengarang('Ani')
    tina = add_pengarang('Tina')

    add_book(cat=novel_cat,
        title="Chicken Soup",
	sinopsis="sdsdsda",
	pengarang=joko)
    add_book(cat=novel_cat,
        title="Perahu Kertas",
	sinopsis="dfdfgf",
	pengarang=budi)

    komik_cat = add_cat("Komik")

    add_book(cat=komik_cat,
        title="Doraemon",
	sinopsis="opopopo",
	pengarang=ani)

    add_book(cat=komik_cat,
        title="Naruto",
	sinopsis="ututut",
	pengarang=joko)

    add_book(cat=komik_cat,
        title="Micko",
	sinopsis="lklklk",
	pengarang=tina)


    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Book.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_book(cat, title, sinopsis, pengarang):
    p = Book.objects.get_or_create(category=cat, title=title)[0]
    p.sinopsis=sinopsis
    p.pengarang=pengarang
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_pengarang(name):
    p = Pengarang.objects.get_or_create(name=name)[0]
    p.save()
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting Buku2 population script..."
    populate()
