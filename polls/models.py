from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class SubmitAttendance(models.Model):

    class Meta:
        db_table = 'polls'

    PLACES = (
        (1, '地球'),
        (2, 'ナメック星'),
        (3, '惑星ベジータ'),
        (4, '惑星フリーザ'),
        (5, '界王星'),
        (6, '界王神界'),
    )
    IN_OUT = (
        (1, '出勤'),
        (0, '退勤'),
    )

    staff = models.ForeignKey(get_user_model(), verbose_name="スタッフ", on_delete=models.CASCADE, default=None)
    place = models.IntegerField(verbose_name='出勤場所名', choices=PLACES, default=None)
    in_out = models.IntegerField(verbose_name='退勤/出勤', choices=IN_OUT, default=None)
    time = models.TimeField(verbose_name="打刻時間")
    date = models.DateField(verbose_name='打刻日')