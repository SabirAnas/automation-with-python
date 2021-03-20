#tihs little project maked by Anas Sabir

#هذه قاعدة بيانات بسيطة لتطبقينا تتضمن اسم الملف وصيغ الملفات التي يجب ان تحتويها
data  = {'pdfs':['pdf'],
         'images':['jpg','png','jpeg','PNG'],
         'exels':['xlsx'],
         'words':['docx'],
         'rars':['rar'],
         'videos':['3gp','mp4'],
         'python':['py'],
         'texts':['txt']}
path = str(input('enter the path of place that u want arrangement it with change \ to / like : xx/xx/xx:'))
import os
os.chdir(f'{path}') #نخصص التطبيق لسطح المكتب فقط عبر هذه الدالة
for elements_in_desktop in os.listdir():
    split_elements = elements_in_desktop.split('.')
    for name_folder in data.keys():
        if split_elements[-1] in data[name_folder]:     #دالة الشرط هنا تبحث عن كل ملف على سطح المكتب و  الملف الدي يجب ان تدخل ايه فان لم يكن ملف خاص بنوع ما تنشأع
            if os.path.exists(name_folder)==True:
                pass
            elif os.path.exists(name_folder) == False :
                os.makedirs(name_folder)
            else:
                pass
            os.rename(elements_in_desktop,f'{name_folder}\\1{elements_in_desktop}')
            os.rename(f'{name_folder}\\1{elements_in_desktop}',f'{name_folder}\\{elements_in_desktop}')
        else:
            pass
print('Done nice desktop :)')
