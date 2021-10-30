# from queues import Queues
from stacks_and_queues.queues import Queues
class AnimalShelter:

    def __init__(self):
        self.cats = Queues()
        self.dogs = Queues()

    def enqueue_Q(self,animal):
        if animal.lower()=="cat" :
            print("inside")
            self.cats.enqueue(animal)
        elif animal.lower()=="dog" :
            self.dogs.enqueue(animal)
        else:
           return 'FOR CATS AND DOGS ONLY'

    def dequeue_Q(self,pref):
        if pref.lower()=="cat":
            return self.cats.dequeue()
        elif pref.lower()=="dog":
            return self.dogs.dequeue()
        else :
            return "NULL,NO DOGS OR CATS FOUND"

    def __str__(self):
        """
        Returns: a string representing the values of front and rear, formatted as:
        "{ c } -> NULL"
        """
        li = []
        cur=self.dogs.rear
        if self.dogs.rear:
            cur = self.dogs.rear
        if self.cats.rear:
            cur = self.cats.rear

        while cur!=None:
            li= li + [(f"{ { cur.value } }").replace("'", " ")]
            cur=cur.next
        return ' -> '.join(li + ["NULL"])

if __name__ == '__main__':
    cats=AnimalShelter()
    # print(dogs.enqueue('mouse'))
    cats.enqueue_Q("cat")
    # print(dogs.dequeue('dogs'))
    print(str(cats))
