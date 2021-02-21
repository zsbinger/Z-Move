# from mongoengine import Document, connect
# from mongoengine import DateTimeField, StringField, ReferenceField, ListField, BooleanField, IntField, ImageField

connect('workouts')

class Workout(Document):
    name = StringField(max_length=60, required=True, unique=False)
    num_rounds = IntField()
    scored = BooleanField()
    content = StringField(required=True, unique=False)
    date = DateTimeField()

    # exercises = ReferenceField(Exercise)

    def __repr__(self):
        return 'Workout: ' + self.name

    def __str__(self):
        # TODO make this more dynamic
        return ''.join(self.name, ': ', str(self.num_rounds), ' rounds of ', str(self.content))


# user of Z-Move
class Mover(Document):
    username = StringField(max_length=25, required=True, unique=True)
    firstname = StringField(max_length=25, required=True, unique=False)
    lastname = StringField(max_length=40, required=True, unique=False)

    # workouts completed
    # TODO
    # workouts created
    # TODO
    # following = ListField()
    # followers = ListField()

    def __repr__(self):
        # TODO make this more appropriate for a repr method
        return 'Mover: ' + self.firstname + ' ' + self.lastname

    def __str__(self):
        return ''.join(self.firstname, ' ', self.lastname, ', ', self.username)


class Exercise(Document):
    name = StringField(max_length=60, required=True, unique=True)
    muscles = ListField()
    demo = ImageField()

    def __repr__(self):
        # TODO make this more appropriate for a repr method
        return ''.join('Exercise: ', self.name, ' working ', str(len(self.muscles)), 'muscle group(s)')

    def __str__(self):
        return ''.join(self.name, ' ', str(self.muscles))
