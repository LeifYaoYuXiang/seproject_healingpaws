# encoding:utf-8
import datetime
import re
import sys

from datetime import timedelta
from imp import reload

from flask import render_template, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

from hospitalapp import app, db
from hospitalapp.form import LoginFrom, RegisterForm, AddPetForm, AddAppointment, MessageForm, ChangeAppointmentState, \
    ReplyForm, AddAppointment_ch, LoginFrom_ch, RegisterForm_ch, AddPetForm_ch, MessageForm_ch, ChangeAppointmentState_ch, ReplyForm_ch

from hospitalapp.models import Staff, Customer, Pet, Message, Reply, Appointment, Video

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

# unregistered customer protocol
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    session['LANGUAGE'] ='EN'

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('index.html', username=username)


@app.route('/index_ch', methods=['GET', 'POST'])
def index_ch():
    session['LANGUAGE'] = 'CH'

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('index_ch.html', username=username)


# unregistered customer protocol
@app.route('/about', methods=['GET', 'POST'])
def about():
    language=session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('about_ch'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('about.html', username=username)


# unregistered customer protocol
@app.route('/about_ch', methods=['GET', 'POST'])
def about_ch():
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('about'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('about_ch.html', username=username)


# unregistered customer protocol
@app.route('/rehabilitation_story', methods=['GET', 'POST'])
def rehabilitation_story():
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('rehabilitation_story_ch'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('rehabilitation_story.html', username=username)


@app.route('/rehabilitation_story_ch', methods=['GET', 'POST'])
def rehabilitation_story_ch():
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('rehabilitation_story'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('rehabilitation_story_ch.html', username=username)


# unregistered customer protocol
@app.route('/retail_store', methods=['GET', 'POST'])
def retail_store():
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('retail_store_ch'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('retail_store.html', username=username)


# unregistered customer protocol
@app.route('/retail_store_ch', methods=['GET', 'POST'])
def retail_store_ch():
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('retail_store'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('retail_store_ch.html', username=username)


# unregistered customer protocol
@app.route('/therapy_team', methods=['GET', 'POST'])
def therapy_team():
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('therapy_team_ch'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('therapy_team.html', username=username)


# unregistered customer protocol
@app.route('/therapy_team_ch', methods=['GET', 'POST'])
def therapy_team_ch():
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('therapy_team'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('therapy_team_ch.html', username=username)


# unregistered customer protocol
@app.route('/treatment_services', methods=['GET', 'POST'])
def treatment_services():
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('treatment_services_ch'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('treatment_services.html', username=username)


# unregistered customer protocol
@app.route('/treatment_services_ch', methods=['GET', 'POST'])
def treatment_services_ch():
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('treatment_services'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('treatment_services_ch.html', username=username)


# unregistered customer protocol
@app.route('/shopping_mall', methods=['GET', 'POST'])
def shopping_mall():
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('shopping_mall_ch'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('shopping_mall.html', username=username)

@app.route('/shopping_mall_ch', methods=['GET', 'POST'])
def shopping_mall_ch():
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('shopping_mall'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    return render_template('shopping_mall_ch.html', username=username)


# unregistered customer protocol
@app.route('/shopping_item/<item_name>', methods=['GET', 'POST'])
def shopping_item(item_name):
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('shopping_item_ch',item_name=item_name))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    product_name = ""
    price = ""
    short_description = ""
    text_description_one = ""
    text_description_two = ""
    image_url =""

    if item_name == 'cat_litter':
        product_name = "Cat Litter"
        price = "$116"
        short_description = "Pidan advanced extreme clumping cat litter with odor control."
        text_description_one = "Improved bean curd cat litter particles, increase the contact area. 5 times the amount of water absorption super province. More firm, More comprehensive package"
        text_description_two = "This is one of our best sellers with a 99% positive rating"
        image_url = "images/shopping_mall/Cat_litter.png"
    elif item_name == 'cat_litter_box':
        product_name = "Cat Litter Box"
        price = "$99"
        short_description = "The best cat litter box. A good quality litter box is a must for any cat owner."
        text_description_one = "Easy to clean; Double door design; Use environmentally friendly materials; The bottom in and out mode can fully release the cat nature, reduce the cat litter out"
        text_description_two = "This is one of our best sellers with a 99% positive rating"
        image_url = "images/shopping_mall/Cat_litter_box.png"
    elif item_name == 'dog_shower_gel':
        product_name = "Dog Shower Gel"
        price = "$128"
        short_description = "Oxyfresh unscented face and body wash for dog, go beyond clean with a shower gel."
        text_description_one = "Extract natural plant essence from natural plant ingredients. Using natural flowers and musk in order to let fragrance more lasting. Innovative moisturizing technology will also improve the ability of cuticle hydration"
        text_description_two = "This is one of our best sellers with a 99% positive rating"
        image_url = "images/shopping_mall/Dog_shower_gel.png"
    elif item_name == 'dog_urine_pad':
        product_name = "Dog Urine Pad"
        price = "$58"
        short_description = "Incontinence Pads|Super Absorbent Protection for puppy|Liquid,Urine,Accidents."
        text_description_one = "Six-layer water lock structure, thickened pad, highly efficient water absorbing molecule. These designs all improve water absorbing speed of diaper"
        text_description_two = "This is one of our best sellers with a 99% positive rating"
        image_url = "images/shopping_mall/Dog_urine_pad.png"
    elif item_name == 'epilation_comb':
        product_name = "Epilation Comb"
        price = "$30.6"
        short_description = "Perfect for large and small breed animals with medium and long coat."
        text_description_one = "The design of fine comb teeth is conducive to let comb teeth deep into the hair root; Non-slip handle design is better for more labor-saving"
        text_description_two = "This is one of our best sellers with a 99% positive rating"
        image_url = "images/shopping_mall/Epilation_comb.png"
    elif item_name == 'pet_waterbowl':
        product_name = "Pet Waterbowl"
        price = "$299"
        short_description = "Get healthy life for our furry guys. get easy life with our furry friends."
        text_description_one = "Five deep purification to let the impurities deep filter. Remove residual chlorine and deep heavy metals. Improve the softening water quality that will effectively prevent pet urinary system diseases"
        text_description_two = "This is one of our best sellers with a 99% positive rating"
        image_url = "images/shopping_mall/Pet_waterbowl.png"
    elif item_name == 'the_cat_climber':
        product_name = "The Cat Climber"
        price = "$300"
        short_description = "51in cat tree tower condo furniture scratch post for kittens pet house play."
        text_description_one = "Cat climbing frame is specially provided for the cat to let him activity entertainment place, good exercise is beneficial to the cat's physical and mental health"
        text_description_two = "This product is one of the best in our shop. Is both practical and practical goods"
        image_url = "images/shopping_mall/The_cat_climber.png"
    elif item_name == 'the_cat_house':
        product_name = "The Cat House"
        price = "$100"
        short_description = "2 big houses are designed for your cat to rest or sleep for privacy."
        text_description_one = "Pure cotton cat house, using the top production technology and production materials. Definitely the best option for your cat"
        text_description_two = "This product is one of the best in our shop. Is both practical and practical goods"
        image_url = "images/shopping_mall/The_cat_house.png"
    elif item_name == 'the_cat_scratch':
        product_name = "The Cat Scratch"
        price = "$150"
        short_description = "Custom made for cats who enjoy scratching, playing and lounging around (What cats don't :)."
        text_description_one = "Scratch boards are used to sharpen a cat's nails to prevent damage to the furniture in the home"
        text_description_two = "This product is one of the best in our shop. Is both practical and practical goods"
        image_url = "images/shopping_mall/The_cat_scratch.png"
    elif item_name == 'the_cat_toy':
        product_name = "The Cat Toy"
        price = "$50"
        short_description = "Cat toys are a fantastic way to keep your kitty entertained, physically active and mentally engaged."
        text_description_one = "A custom made toy that combines your cat's personality and preferences, your cat will love it"
        text_description_two = "This product is one of the best in our shop. Is both practical and practical goods"
        image_url = "images/shopping_mall/The_cat_toy.png"
    elif item_name == 'the_dog_cage':
        product_name = "The Dog Cage"
        price = "$300"
        short_description = "It's not just your dog's cage, we provide a den-like space that your pup can relax in."
        text_description_one = "Pure metal dog cage, strong and reliable, safety first. Can effectively prevent the pet dog out of the situation"
        text_description_two = "This product is one of the best in our shop. Is both practical and practical goods"
        image_url = "images/shopping_mall/The_dog_cage.png"
    else:
        product_name = "The Dog Toy"
        price = "$50"
        short_description = "Finding the right toys for your dog can be tough, we bring you the top toys for your beloved dog."
        text_description_one = "A custom made toy that combines your dog's personality and preferences, your dog will love it"
        text_description_two = "This product is one of the best in our shop. Is both practical and practical goods"
        image_url = "images/shopping_mall/The_dog_toy.png"
    return render_template('shopping_item.html',
                            username=username,
                            product_name=product_name,
                            price=price,
                            short_description=short_description,
                            text_description_one = text_description_one,
                            text_description_two = text_description_two,
                            image_url = image_url,
                        )

@app.route('/shopping_item_ch/<item_name>', methods=['GET', 'POST'])
def shopping_item_ch(item_name):
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('shopping_item',item_name=item_name))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        username = session.get('USERNAME')
    product_name = ""
    price = ""
    short_description = ""
    text_description_one = ""
    text_description_two = ""
    image_url =""

    if item_name == 'cat_litter':
        product_name = "猫砂"
        price = "$116"
        short_description = "皮丹牌先进的带有气味控制的猫砂"
        text_description_one = "改良豆腐猫窝颗粒，增加接触面积。5倍吸水量超省。更坚固，更全面的包装"
        text_description_two = "这是我们的畅销商品之一，99%的好评率"
        image_url = "images/shopping_mall/Cat_litter.png"
    elif item_name == 'cat_litter_box':
        product_name = "猫砂箱"
        price = "$99"
        short_description = "最好的猫砂箱。任何养猫人都必须有一个质量好的猫砂箱"
        text_description_one = "易于清洁；双门设计；采用环保材料；底部进出模式能充分释放猫的天性，减少猫的排泄物"
        text_description_two = "这是我们的畅销商品之一，99%的好评率"
        image_url = "images/shopping_mall/Cat_litter_box.png"
    elif item_name == 'dog_shower_gel':
        product_name = "狗狗沐浴露"
        price = "$128"
        short_description = "为狗狗提供无味的富氧清新沐浴露，使用沐浴露进行清洁"
        text_description_one = "从天然植物成分中提取天然植物精华。使用天然的鲜花和麝香，让香味更持久。创新的保湿技术也会提高角质层的保湿能力"
        text_description_two = "这是我们的畅销商品之一，99%的好评率"
        image_url = "images/shopping_mall/Dog_shower_gel.png"
    elif item_name == 'dog_urine_pad':
        product_name = "狗狗尿垫"
        price = "$58"
        short_description = "尿失禁垫|高吸水性保护小狗|液体，尿液，意外所需"
        text_description_one = "六层锁水结构，加厚垫，高效吸水分子。这些设计都提高了尿布的吸水速度"
        text_description_two = "这是我们的畅销商品之一，99%的好评率"
        image_url = "images/shopping_mall/Dog_urine_pad.png"
    elif item_name == 'epilation_comb':
        product_name = "脱毛梳子"
        price = "$30.6"
        short_description = "非常适合中长毛的大型和小型宠物"
        text_description_one = "精梳齿的设计有利于让梳齿深入发根；防滑手柄设计更省力"
        text_description_two = "这是我们的畅销商品之一，99%的好评率"
        image_url = "images/shopping_mall/Epilation_comb.png"
    elif item_name == 'pet_waterbowl':
        product_name = "宠物饮水器"
        price = "$299"
        short_description = "让我们毛茸茸的家伙过上健康的生活，和我们毛茸茸的朋友过上轻松的生活"
        text_description_one = "五级深度净化，让杂质深度过滤。去除余氯和深层重金属。改善软化水水质，有效预防宠物泌尿系统疾病"
        text_description_two = "这是我们的畅销商品之一，99%的好评率"
        image_url = "images/shopping_mall/Pet_waterbowl.png"
    elif item_name == 'the_cat_climber':
        product_name = "猫爬架"
        price = "$300"
        short_description = "51英寸猫树大厦公寓小猫宠物屋"
        text_description_one = "猫爬架是专门为猫提供活动娱乐场所的，良好的运动有利于猫的身心健康"
        text_description_two = "这个产品是我们店里最好的产品之一。既实惠又实用"
        image_url = "images/shopping_mall/The_cat_climber.png"
    elif item_name == 'the_cat_house':
        product_name = "猫舍"
        price = "$100"
        short_description = "带有2个大房子，为您的猫休息或睡觉而设计的"
        text_description_one = "纯棉猫舍，采用顶级生产工艺和生产材料。对你的猫来说绝对是最好的选择"
        text_description_two = "这个产品是我们店里最好的产品之一。既实惠又实用"
        image_url = "images/shopping_mall/The_cat_house.png"
    elif item_name == 'the_cat_scratch':
        product_name = "猫抓板"
        price = "$150"
        short_description = "为喜欢抓挠、玩耍和闲逛的猫量身定做"
        text_description_one = "猫抓板用来磨快猫的指甲，以防损坏家里的家具"
        text_description_two = "这个产品是我们店里最好的产品之一。既实惠又实用"
        image_url = "images/shopping_mall/The_cat_scratch.png"
    elif item_name == 'the_cat_toy':
        product_name = "猫玩具"
        price = "$50"
        short_description = "猫玩具是一个绝好的方式让你的小猫娱乐，活动身体和投入精神"
        text_description_one = "一个结合你的猫的个性和喜好的定制玩具，你的猫会喜欢的"
        text_description_two = "这个产品是我们店里最好的产品之一。既实惠又实用"
        image_url = "images/shopping_mall/The_cat_toy.png"
    elif item_name == 'the_dog_cage':
        product_name = "狗狗笼子"
        price = "$300"
        short_description = "这不仅仅是一个狗笼，我们提供了一个家一样的空间，让您的小狗可以放松"
        text_description_one = "纯金属狗笼，坚固可靠，安全第一。能有效防止宠物狗出事"
        text_description_two = "这个产品是我们店里最好的产品之一。既实惠又实用"
        image_url = "images/shopping_mall/The_dog_cage.png"
    else:
        product_name = "狗狗玩具"
        price = "$50"
        short_description = "我们能为您的爱犬提供顶级玩具"
        text_description_one = "一个结合你的狗的个性和喜好的定制玩具，你的狗会喜欢的"
        text_description_two = "这个产品是我们店里最好的产品之一。既实惠又实用"
        image_url = "images/shopping_mall/The_dog_toy.png"
    return render_template('shopping_item_ch.html',
                            username=username,
                            product_name=product_name,
                            price=price,
                            short_description=short_description,
                            text_description_one = text_description_one,
                            text_description_two = text_description_two,
                            image_url = image_url,
                        )

# staff protocol
@app.route('/staff', methods=['GET', 'POST'])
def staff():
    session['LANGUAGE'] = 'EN'

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db is None or staff_in_db.staffname != username:
        session.clear()
        return redirect(url_for('login'))
    appointments_array = []
    appointments = Appointment.query.filter().all()
    for appointment in appointments:
        customer = Customer.query.filter(Customer.id == appointment.customer_id).first()
        customer_name = customer.name
        pet = Pet.query.filter(Pet.id == appointment.pet_id).first()
        pet_name = pet.petname
        state = int(appointment.state)
        appointments_array.append(
            {
                'id': appointment.id,
                'customer_name': customer_name,
                'pet_name': pet_name,
                'symptom': appointment.symptom,
                'status': appointment.status,
                'state': state,
                'year': appointment.year,
                'month': appointment.month,
                'date': appointment.date,
            }
        )
    pets_array = []
    pets = Pet.query.filter().all()
    for pet in pets:
        customer = Customer.query.filter(Customer.id == pet.customer_id).first()
        customer_name = customer.name
        if pet.type == '0':
            type = 'cat'
        else:
            type = 'dog'
        pets_array.append(
            {
                'pet_id': pet.id,
                'pet_name': pet.petname,
                'customer_name': customer_name,
                'type': type,
                'age': pet.age,
                'breed': pet.breed,
                }
            )
    num0e=0
    num0s=0
    num1e = 0
    num1s = 0
    num2e = 0
    num2s = 0
    num3e = 0
    num3s = 0
    num4e = 0
    num4s = 0
    num5e = 0
    num5s = 0
    num6e = 0
    num6s = 0
    apps = Appointment.query.all()
    for app in apps:
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==0:
            if app.status=='Emergency':
                num0e=num0e+1
            else:
                num0s=num0s+1
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==1:
            if app.status=='Emergency':
                num1e=num1e+1
            else:
                num1s=num1s+1
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==2:
            if app.status=='Emergency':
                num2e=num2e+1
            else:
                num2s=num2s+1
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==3:
            if app.status=='Emergency':
                num3e=num3e+1
            else:
                num3s=num3s+1
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==4:
            if app.status=='Emergency':
                num4e=num4e+1
            else:
                num4s=num4s+1
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==5:
            if app.status=='Emergency':
                num5e=num5e+1
            else:
                num5s=num5s+1
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==6:
            if app.status=='Emergency':
                num6e=num6e+1
            else:
                num6s=num6s+1
    dog = Pet.query.filter(Pet.type==1).count()
    cat = Pet.query.filter(Pet.type==0).count()
    em = Appointment.query.filter(Appointment.status=='Emergency').count()
    st = Appointment.query.filter(Appointment.status=='Standard').count()
    messages = Message.query.filter().all()
    unread=0
    for message in messages:
        reply = Reply.query.filter(Reply.message_id == message.id).first()
        if reply is None:
            unread=unread+1
    print(unread)
    return render_template('staff.html', appointments_array=appointments_array, pets_array=pets_array, num0e=num0e,num0s=num0s,num1e=num1e,num1s=num1s,num2e=num2e,num2s=num2s,
                           num3s=num3s,num3e=num3e,num4s=num4s,num4e=num4e,num5e=num5e,num5s=num5s,num6e=num6e,num6s=num6s,dog=dog,cat=cat,
                           em=em,st=st, username=username,unread=unread)

# staff protocol
@app.route('/staff_ch', methods=['GET', 'POST'])
def staff_ch():
    session['LANGUAGE'] = 'CH'

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db is None or staff_in_db.staffname != username:
        session.clear()
        return redirect(url_for('login'))
    appointments_array = []
    appointments = Appointment.query.filter().all()
    for appointment in appointments:
        customer = Customer.query.filter(Customer.id == appointment.customer_id).first()
        customer_name = customer.name
        pet = Pet.query.filter(Pet.id == appointment.pet_id).first()
        pet_name = pet.petname
        state = int(appointment.state)
        status = appointment.status
        if status == 'Emergency':
            status = '紧急'
        else:
            status = '标准'
        appointments_array.append(
            {
                'id': appointment.id,
                'customer_name': customer_name,
                'pet_name': pet_name,
                'symptom': appointment.symptom,
                'status': status,
                'state': state,
                'year': appointment.year,
                'month': appointment.month,
                'date': appointment.date,
            }
        )
    pets_array = []
    pets = Pet.query.filter().all()
    for pet in pets:
        customer = Customer.query.filter(Customer.id == pet.customer_id).first()
        customer_name = customer.name
        if pet.type == '0':
            type = '猫猫'
        else:
            type = '狗狗'
        pets_array.append(
            {
                'pet_id': pet.id,
                'pet_name': pet.petname,
                'customer_name': customer_name,
                'type': type,
                'age': pet.age,
                'breed': pet.breed,
                }
            )
    num0e=0
    num0s=0
    num1e = 0
    num1s = 0
    num2e = 0
    num2s = 0
    num3e = 0
    num3s = 0
    num4e = 0
    num4s = 0
    num5e = 0
    num5s = 0
    num6e = 0
    num6s = 0
    apps = Appointment.query.all()
    for app in apps:
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==0:
            if app.status=='Emergency':
                num0e=num0e+1
            else:
                num0s=num0s+1
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==1:
            if app.status=='Emergency':
                num1e=num1e+1
            else:
                num1s=num1s+1
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==2:
            if app.status=='Emergency':
                num2e=num2e+1
            else:
                num2s=num2s+1
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==3:
            if app.status=='Emergency':
                num3e=num3e+1
            else:
                num3s=num3s+1
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==4:
            if app.status=='Emergency':
                num4e=num4e+1
            else:
                num4s=num4s+1
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==5:
            if app.status=='Emergency':
                num5e=num5e+1
            else:
                num5s=num5s+1
        if datetime.datetime.now().year - app.year==0 and datetime.datetime.now().month-app.month==0 and datetime.datetime.now().day-app.date==6:
            if app.status=='Emergency':
                num6e=num6e+1
            else:
                num6s=num6s+1
    dog = Pet.query.filter(Pet.type==1).count()
    cat = Pet.query.filter(Pet.type==0).count()
    em = Appointment.query.filter(Appointment.status=='Emergency').count()
    st = Appointment.query.filter(Appointment.status=='Standard').count()
    messages = Message.query.filter().all()
    unread=0
    for message in messages:
        reply = Reply.query.filter(Reply.message_id == message.id).first()
        if reply is None:
            unread=unread+1
    print(unread)
    return render_template('staff_ch.html', appointments_array=appointments_array, pets_array=pets_array, num0e=num0e,num0s=num0s,num1e=num1e,num1s=num1s,num2e=num2e,num2s=num2s,
                           num3s=num3s,num3e=num3e,num4s=num4s,num4e=num4e,num5e=num5e,num5s=num5s,num6e=num6e,num6s=num6s,dog=dog,cat=cat,
                           em=em,st=st, username=username,unread=unread)


# staff protocol
@app.route('/mailbox', methods=['GET', 'POST'])
def mailbox():
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('mailbox_ch'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db is None or staff_in_db.staffname != username:
        session.clear()
        return redirect(url_for('login'))
    # allmessages = []
    unread_messages = []
    read_messages=[]
    messages = Message.query.filter().all()
    for message in messages:
        temp_id = message.id
        temp_subject = message.subject
        message_year = message.year
        message_month = message.month
        message_date = message.date

        customer = Customer.query.filter(Customer.id == message.customer_id).first()
        customer_name = customer.name

        reply = Reply.query.filter(Reply.message_id == message.id).first()
        if reply is None:
            unread_messages.append(
                {'id': temp_id,
                 'subject': temp_subject,
                 'message_year': message_year,
                 'message_month': message_month,
                 'message_date': message_date,
                 'customer_name': customer_name,
                 }
            )
        if reply is not None:
            read_messages.append(
                {'id': temp_id,
                 'subject': temp_subject,
                 'message_year': message_year,
                 'message_month': message_month,
                 'message_date': message_date,
                 'customer_name': customer_name,
                 }
            )
    length = len(unread_messages)
    return render_template('mailbox.html',
                           size=length,username=username, unread_messages=unread_messages,
                           read_messages=read_messages)


@app.route('/mailbox_ch', methods=['GET', 'POST'])
def mailbox_ch():
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('mailbox'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db is None or staff_in_db.staffname != username:
        session.clear()
        return redirect(url_for('login'))

    unread_messages = []
    read_messages=[]
    messages = Message.query.filter().all()
    for message in messages:
        temp_id = message.id
        temp_subject = message.subject
        message_year = message.year
        message_month = message.month
        message_date = message.date

        customer = Customer.query.filter(Customer.id == message.customer_id).first()
        customer_name = customer.name

        reply = Reply.query.filter(Reply.message_id == message.id).first()
        if reply is None:
            unread_messages.append(
                {'id': temp_id,
                 'subject': temp_subject,
                 'message_year': message_year,
                 'message_month': message_month,
                 'message_date': message_date,
                 'customer_name': customer_name,
                 }
            )
        if reply is not None:
            read_messages.append(
                {'id': temp_id,
                 'subject': temp_subject,
                 'message_year': message_year,
                 'message_month': message_month,
                 'message_date': message_date,
                 'customer_name': customer_name,
                 }
            )
    print(unread_messages)
    length = len(unread_messages)
    return render_template('mailbox_ch.html', unread_messages=unread_messages, read_messages=read_messages, size=length,username=username)

# staff protocol
@app.route('/mail_detail/<id>', methods=['GET', 'POST'])
def mail_detail(id):
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('mail_detail_ch',id=id))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db is None or staff_in_db.staffname != username:
        session.clear()
        return redirect(url_for('login'))
    m = Message.query.filter(Message.id == id).first()
    c = Customer.query.filter(Customer.id == m.customer_id).first()
    message = {'subject': m.subject,
               'year': m.year,
               'month': m.month,
               'date': m.date,
               'customer_name': c.name,
               'content': m.content,
               'id': m.id
               }
    return render_template('mail_detail.html', message=message,username=username)

# staff protocol
@app.route('/mail_detail_ch/<id>', methods=['GET', 'POST'])
def mail_detail_ch(id):
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('mail_detail',id=id))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db is None or staff_in_db.staffname != username:
        session.clear()
        return redirect(url_for('login'))
    m = Message.query.filter(Message.id == id).first()
    c = Customer.query.filter(Customer.id == m.customer_id).first()
    message = {'subject': m.subject,
               'year': m.year,
               'month': m.month,
               'date': m.date,
               'customer_name': c.name,
               'content': m.content,
               'id': m.id
               }
    return render_template('mail_detail_ch.html', message=message,username=username)

# staff protocol
@app.route('/mail_compose/<id>', methods=['GET', 'POST'])
def mail_compose(id):
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('mail_compose_ch',id=id))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db is None or staff_in_db.staffname != username:
        session.clear()
        return redirect(url_for('login'))
    form = ReplyForm()
    m = Message.query.filter(Message.id == id).first()
    customer_id = m.customer_id
    c = Customer.query.filter(Customer.id == customer_id).first()
    email = c.email
    if form.validate_on_submit():
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        date = datetime.datetime.now().day
        reply = Reply(message_id=id, staff_id=userid, content=form.content.data, year=year, month=month, date=date)
        if userid != None:
            db.session.add(reply)
            db.session.commit()
            return redirect(url_for('mailbox'))
        else:
            return redirect(url_for('login'))
    return render_template('mail_compose.html', form=form, email=email, customer_name=c.name, subject=m.subject,username=username)


# staff protocol
@app.route('/mail_compose_ch/<id>', methods=['GET', 'POST'])
def mail_compose_ch(id):
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('mail_compose',id=id))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db is None or staff_in_db.staffname != username:
        session.clear()
        return redirect(url_for('login'))
    form = ReplyForm_ch()
    m = Message.query.filter(Message.id == id).first()
    customer_id = m.customer_id
    c = Customer.query.filter(Customer.id == customer_id).first()
    email = c.email
    if form.validate_on_submit():
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        date = datetime.datetime.now().day
        reply = Reply(message_id=id, staff_id=userid, content=form.content.data, year=year, month=month, date=date)
        if userid != None:
            db.session.add(reply)
            db.session.commit()
            return redirect(url_for('mailbox'))
        else:
            return redirect(url_for('login'))
    return render_template('mail_compose_ch.html', form=form, email=email, customer_name=c.name, subject=m.subject,username=username)

# staff protocol
@app.route('/appointment_detail_staff/<id>', methods=['GET', 'POST'])
def appointment_detail_staff(id):
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('appointment_detail_staff_ch', id=id))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db is None or staff_in_db.staffname != username:
        session.clear()
        return redirect(url_for('login'))

    form = ChangeAppointmentState()
    appointment = Appointment.query.filter(Appointment.id == id).first()
    app_id = id
    customer = Customer.query.filter(Customer.id == appointment.customer_id).first()
    customer_name = customer.name
    pet = Pet.query.filter(Pet.id == appointment.pet_id).first()
    pet_name = pet.petname
    status = appointment.status
    symptom = appointment.symptom
    city = appointment.city

    state_one_year = appointment.year
    state_one_month = appointment.month
    state_one_date = appointment.date

    state_two_year = ""
    state_two_month = ""
    state_two_date = ""
    state_two_description = ""

    state_three_year = ""
    state_three_month = ""
    state_three_date = ""
    state_three_description = ""

    if appointment.state == '2':
        state_two_year = appointment.state_two_year
        state_two_month = appointment.state_two_month
        state_two_date = appointment.state_two_date
        state_two_description = appointment.state_two_description
    if appointment.state == '3':
        state_two_year = appointment.state_two_year
        state_two_month = appointment.state_two_month
        state_two_date = appointment.state_two_date
        state_two_description = appointment.state_two_description

        state_three_year = appointment.state_three_year
        state_three_month = appointment.state_three_month
        state_three_date = appointment.state_three_date
        state_three_description = appointment.state_three_description
    if form.validate_on_submit():
        appointment.state = str(int(appointment.state) + 1)
        print(appointment.state)
        if appointment.state == '2':
            appointment.state_two_year = datetime.datetime.now().year
            appointment.state_two_month = datetime.datetime.now().month
            appointment.state_two_date = datetime.datetime.now().day
            appointment.state_two_description = form.description.data
        elif appointment.state == '3':
            appointment.state_three_year = datetime.datetime.now().year
            appointment.state_three_month = datetime.datetime.now().month
            appointment.state_three_date = datetime.datetime.now().day
            appointment.state_three_description = form.description.data
        video = Video.query.filter(Video.app_id == id).first()
        if video is not None:
            url=form.url.data
            url='https://www.youtube.com/embed/'+url
            video.url=url
            video.app_id=app_id
        else:
            url = form.url.data
            url = 'https://www.youtube.com/embed/' + url
            video=Video(url=url,app_id=app_id)
            db.session.add(video)
        db.session.commit()
        return redirect(url_for('appointment_detail_staff', id=app_id))
    print(state_two_description + "---" + state_three_description)
    return render_template('appointment_detail_staff.html',
                           form=form,
                           id=app_id,
                           customer_name=customer_name,
                           pet_name=pet_name,
                           status=status,
                           state=appointment.state,
                           symptom=symptom,
                           city=city,
                           state_one_year=state_one_year,
                           state_one_month=state_one_month,
                           state_one_date=state_one_date,

                           state_two_year=state_two_year,
                           state_two_month=state_two_month,
                           state_two_date=state_two_date,
                           state_two_description=state_two_description,

                           state_three_year=state_three_year,
                           state_three_month=state_three_month,
                           state_three_date=state_three_date,
                           state_three_description=state_three_description,
                           username=username)

# staff protocol
@app.route('/appointment_detail_staff_ch/<id>', methods=['GET', 'POST'])
def appointment_detail_staff_ch(id):
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('appointment_detail_staff', id=id))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db is None or staff_in_db.staffname != username:
        session.clear()
        return redirect(url_for('login'))

    form = ChangeAppointmentState_ch()
    appointment = Appointment.query.filter(Appointment.id == id).first()
    app_id = id
    customer = Customer.query.filter(Customer.id == appointment.customer_id).first()
    customer_name = customer.name
    pet = Pet.query.filter(Pet.id == appointment.pet_id).first()
    pet_name = pet.petname
    status = appointment.status
    symptom = appointment.symptom
    city = appointment.city
    if city == 'Beijing':
        city = '北京'
    elif city == 'Shanghai':
        city = '上海'
    else:
        city = '成都'

    state_one_year = appointment.year
    state_one_month = appointment.month
    state_one_date = appointment.date

    state_two_year = ""
    state_two_month = ""
    state_two_date = ""
    state_two_description = ""

    state_three_year = ""
    state_three_month = ""
    state_three_date = ""
    state_three_description = ""

    if appointment.state == '2':
        state_two_year = appointment.state_two_year
        state_two_month = appointment.state_two_month
        state_two_date = appointment.state_two_date
        state_two_description = appointment.state_two_description
    if appointment.state == '3':
        state_two_year = appointment.state_two_year
        state_two_month = appointment.state_two_month
        state_two_date = appointment.state_two_date
        state_two_description = appointment.state_two_description

        state_three_year = appointment.state_three_year
        state_three_month = appointment.state_three_month
        state_three_date = appointment.state_three_date
        state_three_description = appointment.state_three_description
    if form.validate_on_submit():
        appointment.state = str(int(appointment.state) + 1)
        print(appointment.state)
        if appointment.state == '2':
            appointment.state_two_year = datetime.datetime.now().year
            appointment.state_two_month = datetime.datetime.now().month
            appointment.state_two_date = datetime.datetime.now().day
            appointment.state_two_description = form.description.data
        elif appointment.state == '3':
            appointment.state_three_year = datetime.datetime.now().year
            appointment.state_three_month = datetime.datetime.now().month
            appointment.state_three_date = datetime.datetime.now().day
            appointment.state_three_description = form.description.data
        video = Video.query.filter(Video.app_id == id).first()
        if video is not None:
            url=form.url.data
            url='https://www.youtube.com/embed/'+url
            video.url=url
            video.app_id=app_id
        else:
            url = form.url.data
            url = 'https://www.youtube.com/embed/' + url
            video=Video(url=url,app_id=app_id)
            db.session.add(video)
        db.session.commit()
        return redirect(url_for('appointment_detail_staff', id=app_id))
    print(state_two_description + "---" + state_three_description)
    return render_template('appointment_detail_staff_ch.html',
                           form=form,
                           id=app_id,
                           customer_name=customer_name,
                           pet_name=pet_name,
                           status=status,
                           state=appointment.state,
                           symptom=symptom,
                           city=city,
                           state_one_year=state_one_year,
                           state_one_month=state_one_month,
                           state_one_date=state_one_date,

                           state_two_year=state_two_year,
                           state_two_month=state_two_month,
                           state_two_date=state_two_date,
                           state_two_description=state_two_description,

                           state_three_year=state_three_year,
                           state_three_month=state_three_month,
                           state_three_date=state_three_date,
                           state_three_description=state_three_description,
                           username=username)


# staff protocol
@app.route('/staff_petinfo/<id>',methods=['GET','POST'])
def staff_petinfo(id):
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('staff_petinfo_ch', id=id))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db is None or staff_in_db.staffname != username:
        session.clear()
        return redirect(url_for('login'))

    pet = Pet.query.filter(Pet.id == id).first()
    customer = Customer.query.filter(Customer.id == pet.customer_id).first()
    customer_name = customer.name
    pet_name = pet.petname
    pet_id = id
    if pet.type == '0':
        type = 'cat'
    else:
        type = 'dog'
    age = pet.age
    breed = pet.breed

    aapps = []
    apps = Appointment.query.filter(Appointment.pet_id == id).all()
    if apps is not None:
        for app in apps:
            if app.state == '1':
                aapps.append(
                    {
                     'year': app.year,
                     'month': app.month,
                     'date': app.date,
                     'symptom': app.symptom,
                     'state': 'State 1:Waiting',
                     }
                )
            elif app.state == '2':
                aapps.append(
                    {
                     'year': app.year,
                     'month': app.month,
                     'date': app.date,
                     'symptom': app.symptom,
                     'state': 'State 2:Curing',
                     }
                )
            else:
                aapps.append(
                    {
                     'year': app.year,
                     'month': app.month,
                     'date': app.date,
                     'symptom': app.symptom,
                     'state': 'State 3:Recovering',
                     }
                )
    else:
        aapps=[]

    return render_template('staff_petinfo.html',
                           id=pet_id,
                           customer_name=customer_name,
                           pet_name=pet_name,
                           type=type,
                           age=age,
                           breed=breed,
                           aapps=aapps,
                           username=username)


# staff protocol
@app.route('/staff_petinfo_ch/<id>',methods=['GET','POST'])
def staff_petinfo_ch(id):
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('staff_petinfo', id=id))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db is None or staff_in_db.staffname != username:
        session.clear()
        return redirect(url_for('login'))

    pet = Pet.query.filter(Pet.id == id).first()
    customer = Customer.query.filter(Customer.id == pet.customer_id).first()
    customer_name = customer.name
    pet_name = pet.petname
    pet_id = id
    if pet.type == '0':
        type = '猫猫'
    else:
        type = '狗狗'
    age = pet.age
    breed = pet.breed

    aapps = []
    apps = Appointment.query.filter(Appointment.pet_id == id).all()
    if apps is not None:
        for app in apps:
            if app.state == '1':
                aapps.append(
                    {
                     'year': app.year,
                     'month': app.month,
                     'date': app.date,
                     'symptom': app.symptom,
                     'state': 'State 1:Waiting',
                     }
                )
            elif app.state == '2':
                aapps.append(
                    {
                     'year': app.year,
                     'month': app.month,
                     'date': app.date,
                     'symptom': app.symptom,
                     'state': 'State 2:Curing',
                     }
                )
            else:
                aapps.append(
                    {
                     'year': app.year,
                     'month': app.month,
                     'date': app.date,
                     'symptom': app.symptom,
                     'state': 'State 3:Recovering',
                     }
                )
    else:
        aapps=[]

    return render_template('staff_petinfo_ch.html',
                           id=pet_id,
                           customer_name=customer_name,
                           pet_name=pet_name,
                           type=type,
                           age=age,
                           breed=breed,
                           aapps=aapps,
                           username=username)


# registered customer protocol
@app.route('/personal_information', methods=['GET', 'POST'])
def personal_information():
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('personal_information_ch'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        return redirect(url_for('login'))
    pet_in_db = []
    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    customer_in_db = Customer.query.filter(Customer.id == userid).first()
    if customer_in_db is None:
        return redirect(url_for('login'))
    icon = username[0].upper()
    print(icon)
    icon = "images/icon/"+icon+".png"
    dog_num = 0
    cat_num = 0
    form = AddPetForm()
    pets = Pet.query.filter(Pet.customer_id == userid).all()
    for pet in pets:
        type = 'Dog'
        if pet.type == '0':
            type = 'Cat'
            cat_num=cat_num+1
        else:
            dog_num=dog_num+1
        pet_in_db.append(
            {'name': pet.petname,
             'age': pet.age,
             'breed': pet.breed,
             'type': type}
        )
    if form.validate_on_submit():
        new_pet = Pet(customer_id=userid,
                        type=form.type.data,
                        petname=form.name.data,
                        age=form.age.data,
                        breed=form.breed.data,
                        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('personal_information'))
    return render_template('personal_information.html',
                           username=username,
                           email=customer_in_db.email,
                           form=form,
                           pets=pet_in_db,
                           icon=icon,
                           cat_num=cat_num,
                           dog_num=dog_num)

# registered customer protocol
@app.route('/personal_information_ch', methods=['GET', 'POST'])
def personal_information_ch():
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('personal_information'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        return redirect(url_for('login'))
    pet_in_db = []
    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    customer_in_db = Customer.query.filter(Customer.id == userid).first()
    if customer_in_db is None:
        return redirect(url_for('login'))
    icon = username[0].upper()
    icon = "images/icon/"+icon+".png"
    dog_num = 0
    cat_num = 0
    form = AddPetForm_ch()
    pets = Pet.query.filter(Pet.customer_id == userid).all()
    for pet in pets:
        type = 'Dog'
        if pet.type == '0':
            type = 'Cat'
            cat_num=cat_num+1
        else:
            dog_num=dog_num+1
        pet_in_db.append(
            {'name': pet.petname,
             'age': pet.age,
             'breed': pet.breed,
             'type': type}
        )
    if form.validate_on_submit():
        new_pet = Pet(customer_id=userid,
                      type=form.type.data,
                      petname=form.name.data,
                      age=form.age.data,
                      breed=form.breed.data,
                      )
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('personal_information'))
    return render_template('personal_information_ch.html',
                           username=username,
                           email=customer_in_db.email,
                           form=form,
                           pets=pet_in_db,
                           icon=icon,
                           cat_num=cat_num,
                           dog_num=dog_num)


# registered customer protocol
@app.route('/message_square', methods=['GET', 'POST'])
def message_square():
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('message_square_ch'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        return redirect(url_for('login'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    customer_in_db = Customer.query.filter(Customer.id == userid).first()
    if customer_in_db is None:
        return redirect(url_for('login'))

    form = MessageForm()
    message_and_reply = []
    feedback_list = []
    messages = Message.query.filter().all()

    for message in messages:
        temp_subject = message.subject
        temp_content = message.content
        message_year = message.year
        message_month = message.month
        message_date = message.date

        customer = Customer.query.filter(Customer.id == message.customer_id).first()

        customer_name = customer.name
        icon = customer_name[0].upper()
        icon = "images/icon/" + icon + ".png"

        reply = Reply.query.filter(Reply.message_id == message.id).first()
        reply_year = ''
        reply_month = ''
        reply_date = ''
        staff_name = ''
        reply_content = ''
        if reply is not None:
            reply_year = reply.year
            reply_month = reply.month
            reply_date = reply.date
            reply_content = reply.content
            staff = Staff.query.filter(Staff.id == reply.staff_id).first()
            staff_name = staff.staffname

            if userid == customer.id:
                feedback_list.append(
                    {'subject': temp_subject,
                     'reply_year': reply_year,
                     'reply_month': reply_month,
                     'reply_date': reply_date,
                     'reply_content': reply_content
                     }
                )

        message_and_reply.append(
            {'subject': temp_subject,
             'content': temp_content,
             'message_year': message_year,
             'message_month': message_month,
             'message_date': message_date,
             'customer_name': customer_name,
             'staff_name': staff_name,
             'reply_year': reply_year,
             'reply_month': reply_month,
             'reply_date': reply_date,
             'reply_content': reply_content,
             'icon':icon
             }
        )


    if form.validate_on_submit():
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        new_message = Message(customer_id=userid,
                              subject=form.subject.data,
                              content=form.content.data,
                              year=year,
                              month=month,
                              date=day)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('message_square'))

    return render_template('message_square.html',
                           username=username,
                           form=form,
                           message_and_reply=message_and_reply,
                           feedbacks=feedback_list)


@app.route('/message_square_ch', methods=['GET', 'POST'])
def message_square_ch():
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('message_square'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        return redirect(url_for('login'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    customer_in_db = Customer.query.filter(Customer.id == userid).first()
    if customer_in_db is None:
        return redirect(url_for('login'))

    form = MessageForm_ch()
    message_and_reply = []
    feedback_list = []
    messages = Message.query.filter().all()

    for message in messages:
        temp_subject = message.subject
        temp_content = message.content
        message_year = message.year
        message_month = message.month
        message_date = message.date

        customer = Customer.query.filter(Customer.id == message.customer_id).first()

        customer_name = customer.name
        icon = customer_name[0].upper()
        icon = "images/icon/" + icon + ".png"

        reply = Reply.query.filter(Reply.message_id == message.id).first()
        reply_year = ''
        reply_month = ''
        reply_date = ''
        staff_name = ''
        reply_content = ''
        if reply is not None:
            reply_year = reply.year
            reply_month = reply.month
            reply_date = reply.date
            reply_content = reply.content
            staff = Staff.query.filter(Staff.id == reply.staff_id).first()
            staff_name = staff.staffname

            if userid == customer.id:
                feedback_list.append(
                    {'subject': temp_subject,
                     'reply_year': reply_year,
                     'reply_month': reply_month,
                     'reply_date': reply_date,
                     'reply_content': reply_content
                     }
                )

        message_and_reply.append(
            {'subject': temp_subject,
             'content': temp_content,
             'message_year': message_year,
             'message_month': message_month,
             'message_date': message_date,
             'customer_name': customer_name,
             'staff_name': staff_name,
             'reply_year': reply_year,
             'reply_month': reply_month,
             'reply_date': reply_date,
             'reply_content': reply_content,
             'icon':icon
             }
        )


    if form.validate_on_submit():
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        new_message = Message(customer_id=userid,
                              subject=form.subject.data,
                              content=form.content.data,
                              year=year,
                              month=month,
                              date=day)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('message_square_ch'))

    return render_template('message_square_ch.html',
                           username=username,
                           form=form,
                           message_and_reply=message_and_reply,
                           feedbacks=feedback_list)


# registered customer protocol
@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('appointment_ch'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        return redirect(url_for('login'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    customer_in_db = Customer.query.filter(Customer.id == userid).first()
    if customer_in_db is None:
        return redirect(url_for('login'))


    form = AddAppointment()
    pet_in_db = []
    pets = Pet.query.filter(Pet.customer_id == userid).all()
    for pet in pets:
        pet_in_db.append(
            ((str(pet.id), pet.petname))
        )
    form.pet.choices = pet_in_db

    if form.validate_on_submit():
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        date = datetime.datetime.now().day
        # apptime=datetime.datetime.now()
        ap = Appointment(customer_id=userid, state=1, pet_id=form.pet.data, symptom=form.symptom.data,
                         status=form.service.data, city=form.city.data,
                         year=year, month=month, date=date)
        db.session.add(ap)
        db.session.commit()

    aapps = []
    apps = Appointment.query.filter(Appointment.customer_id == userid).all()
    for app in apps:
        pet = Pet.query.filter(Pet.id == app.pet_id).first()
        petname = pet.petname
        if app.state == '1':
            aapps.append(
                {
                 'petname': petname,
                 'year': app.year,
                 'month': app.month,
                 'date': app.date,
                 'symptom': app.symptom,
                 'state': 'State 1:Waiting',
                 'id': app.id,
                 }
            )
        elif app.state == '2':
            aapps.append(
                {
                 'petname': petname,
                 'year': app.year,
                 'month': app.month,
                 'date': app.date,
                 'symptom': app.symptom,
                 'state': 'State 2:Curing',
                 'id': app.id
                 }
            )
        else:
            aapps.append(
                {
                 'petname': petname,
                 'year': app.year,
                 'month': app.month,
                 'date': app.date,
                 'symptom': app.symptom,
                 'state': 'State 3:Recovering',
                 'id': app.id,
                 }
            )
    return render_template('appointment.html', aapps=aapps, username=username, form=form)


@app.route('/appointment_ch', methods=['GET', 'POST'])
def appointment_ch():
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('appointment'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')

    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        return redirect(url_for('login'))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    customer_in_db = Customer.query.filter(Customer.id == userid).first()
    if customer_in_db is None:
        return redirect(url_for('login'))


    form = AddAppointment_ch()
    pet_in_db = []
    pets = Pet.query.filter(Pet.customer_id == userid).all()
    for pet in pets:
        pet_in_db.append(
            ((str(pet.id), pet.petname))
        )
    form.pet.choices = pet_in_db

    if form.validate_on_submit():
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        date = datetime.datetime.now().day
        # apptime=datetime.datetime.now()
        ap = Appointment(customer_id=userid, state=1, pet_id=form.pet.data, symptom=form.symptom.data,
                         status=form.service.data, city=form.city.data,
                         year=year, month=month, date=date)
        db.session.add(ap)
        db.session.commit()

    aapps = []
    apps = Appointment.query.filter(Appointment.customer_id == userid).all()
    for app in apps:
        pet = Pet.query.filter(Pet.id == app.pet_id).first()
        petname = pet.petname
        if app.state == '1':
            aapps.append(
                {
                 'petname': petname,
                 'year': app.year,
                 'month': app.month,
                 'date': app.date,
                 'symptom': app.symptom,
                 'state': 'State 1:Waiting',
                 'id': app.id,
                 }
            )
        elif app.state == '2':
            aapps.append(
                {
                 'petname': petname,
                 'year': app.year,
                 'month': app.month,
                 'date': app.date,
                 'symptom': app.symptom,
                 'state': 'State 2:Curing',
                 'id': app.id
                 }
            )
        else:
            aapps.append(
                {
                 'petname': petname,
                 'year': app.year,
                 'month': app.month,
                 'date': app.date,
                 'symptom': app.symptom,
                 'state': 'State 3:Recovering',
                 'id': app.id,
                 }
            )
    return render_template('appointment_ch.html', aapps=aapps, username=username, form=form)

# registered customer protocol
@app.route('/appointment_detail/<id>/', methods=['GET', 'POST'])
def appointment_detail(id):

    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('appointment_detail_ch',id=id))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        return redirect(url_for('login'))
    userid = session.get('USER_ID')
    customer_in_db = Customer.query.filter(Customer.id == userid).first()
    if customer_in_db is None:
        return redirect(url_for('login'))


    url= 'https://www.youtube.com/embed/qrD5SyYb1Ck'
    appointment = Appointment.query.filter(Appointment.id == id).first()
    video = Video.query.filter(Video.app_id == id).first()
    if video is not None:
        url=video.url
    appointment_id = appointment.id
    customer = Customer.query.filter(Customer.id == appointment.customer_id).first()
    customer_name = customer.name
    pet = Pet.query.filter(Pet.id == appointment.pet_id).first()
    pet_name = pet.petname
    status = appointment.status
    symptom = appointment.symptom
    city = appointment.city

    state_one_year = appointment.year
    state_one_month = appointment.month
    state_one_date = appointment.date

    state_two_year = ""
    state_two_month = ""
    state_two_date = ""
    state_two_description = ""

    state_three_year = ""
    state_three_month = ""
    state_three_date = ""
    state_three_description = ""

    if appointment.state == '2':
        state_two_year = appointment.state_two_year
        state_two_month = appointment.state_two_month
        state_two_date = appointment.state_two_date
        state_two_description = appointment.state_two_description
    if appointment.state == '3':
        state_two_year = appointment.state_two_year
        state_two_month = appointment.state_two_month
        state_two_date = appointment.state_two_date
        state_two_description = appointment.state_two_description

        state_three_year = appointment.state_three_year
        state_three_month = appointment.state_three_month
        state_three_date = appointment.state_three_date
        state_three_description = appointment.state_three_description
    return render_template('appointment_detail.html',
                           username = username,
                           appointment_id=appointment_id,
                           customer_name=customer_name,
                           pet_name=pet_name,
                           state=appointment.state,
                           symptom=symptom,
                           city=city,
                           state_one_year=state_one_year,
                           state_one_month=state_one_month,
                           state_one_date=state_one_date,

                           state_two_year=state_two_year,
                           state_two_month=state_two_month,
                           state_two_date=state_two_date,
                           state_two_description=state_two_description,

                           state_three_year=state_three_year,
                           state_three_month=state_three_month,
                           state_three_date=state_three_date,
                           state_three_description=state_three_description,
                           url=url)


@app.route('/appointment_detail_ch/<id>/', methods=['GET', 'POST'])
def appointment_detail_ch(id):
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('appointment_detail',id=id))

    username = session.get('USERNAME')
    userid = session.get('USER_ID')
    staff_in_db = Staff.query.filter(Staff.id == userid).first()
    if staff_in_db and staff_in_db.staffname == username:
        session.clear()
        return redirect(url_for('login'))
    userid = session.get('USER_ID')
    customer_in_db = Customer.query.filter(Customer.id == userid).first()
    if customer_in_db is None:
        return redirect(url_for('login'))

    url= 'https://www.youtube.com/embed/qrD5SyYb1Ck'
    appointment = Appointment.query.filter(Appointment.id == id).first()
    video = Video.query.filter(Video.app_id == id).first()
    if video is not None:
        url=video.url
    appointment_id = appointment.id
    customer = Customer.query.filter(Customer.id == appointment.customer_id).first()
    customer_name = customer.name
    pet = Pet.query.filter(Pet.id == appointment.pet_id).first()
    pet_name = pet.petname
    status = appointment.status
    symptom = appointment.symptom
    city = appointment.city
    if city == 'Beijing':
        city = '北京'
    elif city == 'Shanghai':
        city = '上海'
    else:
        city = '成都'

    state_one_year = appointment.year
    state_one_month = appointment.month
    state_one_date = appointment.date

    state_two_year = ""
    state_two_month = ""
    state_two_date = ""
    state_two_description = ""

    state_three_year = ""
    state_three_month = ""
    state_three_date = ""
    state_three_description = ""

    if appointment.state == '2':
        state_two_year = appointment.state_two_year
        state_two_month = appointment.state_two_month
        state_two_date = appointment.state_two_date
        state_two_description = appointment.state_two_description
    if appointment.state == '3':
        state_two_year = appointment.state_two_year
        state_two_month = appointment.state_two_month
        state_two_date = appointment.state_two_date
        state_two_description = appointment.state_two_description

        state_three_year = appointment.state_three_year
        state_three_month = appointment.state_three_month
        state_three_date = appointment.state_three_date
        state_three_description = appointment.state_three_description
    return render_template('appointment_detail_ch.html',
                           username = username,
                           appointment_id=appointment_id,
                           customer_name=customer_name,
                           pet_name=pet_name,
                           state=appointment.state,
                           symptom=symptom,
                           city=city,
                           state_one_year=state_one_year,
                           state_one_month=state_one_month,
                           state_one_date=state_one_date,

                           state_two_year=state_two_year,
                           state_two_month=state_two_month,
                           state_two_date=state_two_date,
                           state_two_description=state_two_description,

                           state_three_year=state_three_year,
                           state_three_month=state_three_month,
                           state_three_date=state_three_date,
                           state_three_description=state_three_description,
                           url=url
                           )


# staff&customer protocol
@app.route('/login', methods=['GET', 'POST'])
def login():
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('login_ch'))

    form = LoginFrom()
    if form.validate_on_submit():
        staff_in_db = Staff.query.filter(Staff.staffname == form.username.data).first()
        if not staff_in_db:
            customer_in_db = Customer.query.filter(Customer.name == form.username.data).first()
            if not customer_in_db:
                flash('No User Found')
                return redirect(url_for('login'))
            if check_password_hash(customer_in_db.password_hash, form.password.data):
                print('Login Success')
                session['USERNAME'] = customer_in_db.name
                session['USER_ID'] = customer_in_db.id
                session['LANGUAGE'] = 'EN'
                return redirect(url_for("index"))
            flash('Incorrect Password')
            return redirect(url_for('login'))
        if staff_in_db.password_hash == form.password.data:
            print('Login Success')
            session['USERNAME'] = staff_in_db.staffname
            session['USER_ID'] = staff_in_db.id
            session['LANGUAGE'] = 'EN'
            return redirect(url_for('staff'))
    return render_template('login.html', form=form)


@app.route('/login_ch', methods=['GET', 'POST'])
def login_ch():
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('login'))
    form = LoginFrom_ch()
    if form.validate_on_submit():
        staff_in_db = Staff.query.filter(Staff.staffname == form.username.data).first()
        if not staff_in_db:
            customer_in_db = Customer.query.filter(Customer.name == form.username.data).first()
            if not customer_in_db:
                flash('用户不存在')
                return redirect(url_for('login'))
            if check_password_hash(customer_in_db.password_hash, form.password.data):
                print('登录成功')
                session['USERNAME'] = customer_in_db.name
                session['USER_ID'] = customer_in_db.id
                session['LANGUAGE'] = 'CH'
                return redirect(url_for("index_ch"))
            flash('密码不正确')
            return redirect(url_for('login'))
        if staff_in_db.password_hash == form.password.data:
            print('登录成功')
            session['USERNAME'] = staff_in_db.staffname
            session['USER_ID'] = staff_in_db.id
            session['LANGUAGE'] = 'CH'
            return redirect(url_for('staff'))
    return render_template('login_ch.html', form=form)


# staff&customer protocol
@app.route('/register', methods=['GET', 'POST'])
def register():
    language = session.get('LANGUAGE')
    if language == 'CH':
        return redirect(url_for('register_ch'))

    form = RegisterForm()
    if form.validate_on_submit():
        staff_in_db = Staff.query.filter(Staff.staffname == form.username.data).first()
        customer_in_db = Customer.query.filter(Customer.name == form.username.data).first()
        if not staff_in_db and not customer_in_db:
            re_email = re.compile(r'^([a-zA-Z\.0-9]+)@[a-zA-Z0-9]+\.[a-zA-Z]{3}$')
            email_in_db_staff = Staff.query.filter(Staff.email == form.email.data).first()
            email_in_db_customer = Customer.query.filter(Customer.email == form.email.data).first()
            if not email_in_db_staff and not email_in_db_customer:
                if re_email.match(form.email.data):
                    print('email format is correct')
                    password_hash = generate_password_hash(form.password.data)
                    user = Customer(name=form.username.data, email=form.email.data, password_hash=password_hash)
                    db.session.add(user)
                    db.session.commit()
                    session["USERNAME"] = user.name
                    session['USERID'] = user.id
                    session['LANGUAGE'] = 'EN'
                    flash('Register Success')
                    return redirect(url_for('personal_information'))
                flash('Incorrect Email Format')
                return redirect(url_for('register'))
            flash('Email Has Already Exist')
            return redirect(url_for('register'))
        flash('Username Has Already Exist')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)


@app.route('/register_ch', methods=['GET', 'POST'])
def register_ch():
    language = session.get('LANGUAGE')
    if language == 'EN':
        return redirect(url_for('register'))

    form = RegisterForm_ch()
    if form.validate_on_submit():
        staff_in_db = Staff.query.filter(Staff.staffname == form.username.data).first()
        customer_in_db = Customer.query.filter(Customer.name == form.username.data).first()
        if not staff_in_db and not customer_in_db:
            re_email = re.compile(r'^([a-zA-Z\.0-9]+)@[a-zA-Z0-9]+\.[a-zA-Z]{3}$')
            email_in_db_staff = Staff.query.filter(Staff.email == form.email.data).first()
            email_in_db_customer = Customer.query.filter(Customer.email == form.email.data).first()
            if not email_in_db_staff and not email_in_db_customer:
                if re_email.match(form.email.data):
                    print('email format is correct')
                    password_hash = generate_password_hash(form.password.data)
                    user = Customer(name=form.username.data, email=form.email.data, password_hash=password_hash)
                    db.session.add(user)
                    db.session.commit()
                    session["USERNAME"] = user.name
                    session['USERID'] = user.id
                    session['LANGUAGE'] = 'CH'
                    flash('注册成功')
                    return redirect(url_for('personal_information'))
                flash('邮箱格式不正确')
                return redirect(url_for('register_ch'))
            flash('邮箱已被注册')
            return redirect(url_for('register_ch'))
        flash('用户名已被注册')
        return redirect(url_for('register_ch'))
    return render_template('register_ch.html', form=form)


# staff&customer protocol
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return render_template('index.html')


@app.route('/reference', methods=['GET', 'POST'])
def reference():
    return render_template('reference.html')



