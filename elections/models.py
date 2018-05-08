from django.db import models

# Create your models here.

# 선거 후보자들
class Candidate(models.Model):
    name=models.CharField(max_length=10)
    introduction=models.TextField()
    area=models.CharField(max_length=15)
    party_number=models.IntegerField(default=0)

    def __str__(self):
        return self.name


# 여론조사
class Poll(models.Model):
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    area=models.CharField(max_length=15)


# 후보 여론조사 결과
class Choice(models.Model):
    poll=models.ForeignKey(Poll, on_delete=models.CASCADE)
    candidate=models.ForeignKey(Candidate, on_delete=models.DO_NOTHING)
    votes=models.IntegerField(default=0)
<<<<<<< HEAD

    def __str__(self):
        return self.candidate.name
=======
>>>>>>> 092de09f46b700174268e7cf56189b4019d7f23d
