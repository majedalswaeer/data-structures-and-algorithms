from .hash_table import HashTable
import re
def hashmap_repeated_word(my_str):
    my_new_string = re.sub('[^a-zA-Z0-9 \n.]', '', my_str).lower()
    splitted=my_new_string.split(' ')
    ins=HashTable()
    for i in splitted:
        if ins.contains(i):
            return(i)
        ins.add(i,i)




if __name__ == '__main__':
    x='It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
    print(hashmap_repeated_word(x))

