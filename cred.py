from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def App():
    put_html('<center>استمارة الطالب المقبول<h3></h3></center>').style('background-color:#277BC0; color:gold; padding:20px;')
    put_html('<p>تم برمجة الموقع من قبل مرتضى كريم</p>').style('text-align:center;')
    put_html('<p>تصدير السيرة الذاتية للطلاب</p>').style('text-align:center; font-weight:bold;')
    put_html('<center> <img src="https://3.bp.blogspot.com/-YfZBAem3KyQ/UQgmVpNCj8I/AAAAAAAAAK8/qbM8v_RLaCI/s1600/students.jpg" width=""> </center>')
    data = input_group(
        'ملئ استمارة الطالب المتفوق المؤهل',
        [
            input('اسم الطالب' , name='student'),
            input('عنوان الطالب' , name='country'),
            input('بريد الأكتروني' , name='email'),
            input('رقم الهاتف' , name='phone', type=NUMBER),
            radio('مؤهلات الطالب' , options=['word','excel','powerpoin'],name='certi'),
            checkbox('اتقان اللغات' , options=['عربي','انكليزي','فرنسي'],inline=True , name='lang')
        ],
    )
    imgs = file_upload(
        'تحميل صورة الطالب',
        accept='imge/*',
        multiple=True
    )
    for img in imgs:
        global rr
        rr = img['content']

        put_text('student cv :')
        put_table([
            ['stdentImg','Name','Address', 'phone', 'certificate', 'language'],
            [put_image(rr).style('width:50px;'),data['student'],data['country'],data['phone'],data['certi'],data['lang']]
        ])



start_server(App , port=3335 , debug=True)
