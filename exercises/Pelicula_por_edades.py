# https://pywombat.com/my/exercises/75b6ab38

from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = """
    <table>
        <thead>
            <tr>
                <th>Rango de edad</th>
                <th>Película</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><16</td>
                <td>"Coco"</td>
            </tr>
            <tr>
                <td>17 -- 25</td>
                <td>"Avengers: Endgame"</td>
            </tr>
            <tr>
                <td>26 -- 40</td>
                <td>"Matrix"</td>
            </tr>
            <tr>
                <td>41 -- 60</td>
                <td>"El libro verde"</td>
            </tr>
            <tr>
                <td>>60</td>
                <td>"Un golpe con estilo"</td>
            </tr>
        </tbody>
    </table>
    """

    input_age = int(input('Edad: '))

    soup = BeautifulSoup(html, 'html.parser')
    trs = soup.table.tbody.find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        age = tds[0].get_text()
        movie = tds[1].get_text()

        if '<' in age: 
            if input_age < int(age.split('<')[1]):
                result = movie
        elif '>' in age:
            if input_age > int(age.split('>')[1]):
                result = movie
        else:
            start, end = age.split(' -- ')
            if int(start) < input_age and input_age < int(end):
                result = movie
    print(result)
