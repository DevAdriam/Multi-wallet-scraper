from bs4 import BeautifulSoup

with open('./html/home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')

    course_cards = soup.findAll("div", class_="card")
    for card in course_cards:
        course_title = card.h5.text
        course_price = card.a.text.split()[2]

        print(f'{course_title} costs {course_price}')
