from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class SubmitAttendance(models.Model):

    class Meta:
        db_table = 'polls'

    PLACES = (
        (1, '愛工大名電高校'),
        (2, '中部大学'),
        (3, '新潟大学'),
        (4, '新潟大学院'),
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