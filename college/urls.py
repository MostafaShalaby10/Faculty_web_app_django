from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home , name="showhome"),
    path('showstudents/deletestudents/<int:id>',views.deletestudents , name="deletestudents"),
    path('showsubjects/deletesubjects/<int:id>',views.deletesubjects , name="deletesubjects"),
    path('showtracks/deletetracks/<int:id>',views.deletetracks , name="deletetracks"),
    path('showexams/deleteexam/<int:id>',views.deleteexam , name="deleteexam"),
    path('showstudents/',views.showstudents , name="showstudents"),
    path('showtracks/',views.showtracks , name="showtracks"),
    path('showsubjects/',views.showsubjects , name="showsubjects"),
    path('showexams/',views.showexams , name="showexams"),
    path('insertstudents/',views.insertstudents , name="insertstudents"),
    path('insertsubjects/',views.insertsubjects , name="insertsubjects"),
    path('insertexam/',views.insertexam , name="insertexam"),
    path('inserttracks/',views.inserttracks , name="inserttracks"),
    path('showstudents/editstudents/<int:id>',views.editstudents , name="editstudents"),
    path('showsubjects/editsubjects/<int:id>',views.editsubjects , name="editsubjects"),
    path('showtracks/edittracks/<int:id>',views.edittracks , name="edittracks"),
    path('showexams/editexam/<int:id>',views.editexam , name="editexam"),
    path('showstudents/editstudents/updatestudents/<int:id>',views.updatestudents , name="updatestudents"),
    path('showsubjects/editsubjects/updatesubjects/<int:id>',views.updatesubjects , name="updatesubjects"),
    path('showexams/editexam/updateexam/<int:id>',views.updateexam , name="updateexam"),
    path('showtracks/edittracks/updatetracks/<int:id>',views.updatetracks , name="updatetracks"),
]