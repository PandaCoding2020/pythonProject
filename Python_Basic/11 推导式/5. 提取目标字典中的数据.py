counts = {'MBP':286,'HP':125,'DELL':201,'Lenovo':199,'acer':99,'Apple':298,'IBM':276,}

count1 = {key:value for key,value in counts.items() if value>=200}
print(count1)