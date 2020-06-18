# encoding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, IntegerField, \
    SelectField
from wtforms.validators import DataRequired, NumberRange


class LoginFrom(FlaskForm):
    username = StringField('Username', validators=[DataRequired()],render_kw={"placeholder": "your name"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "your password"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class LoginFrom_ch(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()],render_kw={"placeholder": "您的名字"})
    password = PasswordField('密码', validators=[DataRequired()],render_kw={"placeholder": "您的密码"})
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()],render_kw={"placeholder": "your username"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "your password"})
    email = StringField('Email', validators=[DataRequired()],render_kw={"placeholder": "your email"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')

class RegisterForm_ch(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()],render_kw={"placeholder": "您的名字"})
    password = PasswordField('密码', validators=[DataRequired()],render_kw={"placeholder": "您的密码"})
    email = StringField('邮箱', validators=[DataRequired()],render_kw={"placeholder": "您的邮箱"})
    remember_me = BooleanField('记住我')
    submit = SubmitField('注册')

class AddPetForm(FlaskForm):
    # type = RadioField('Species', choices=[('0', 'Cat'), ('1', 'Dog')], validators=[DataRequired()])
    type=SelectField('Species', validators=[DataRequired()], choices=[('0', 'Cat'), ('1', 'Dog')])
    name = StringField('Your Pet Name', validators=[DataRequired()], render_kw={"placeholder": "your pet name"})
    age = IntegerField('Your Pet Age', validators=[DataRequired(message='Positive integer is required!'), NumberRange(min=0)],render_kw={"placeholder": "your pet age"})
    breed = StringField('Your Pet Breed', validators=[DataRequired()], render_kw={"placeholder": "your pet breed"})
    submit = SubmitField('Add My Pet')

class AddPetForm_ch(FlaskForm):
    # type = RadioField('Species', choices=[('0', 'Cat'), ('1', 'Dog')], validators=[DataRequired()])
    type=SelectField('猫猫还是狗狗', validators=[DataRequired()], choices=[('0', '猫猫'), ('1', '狗狗')])
    name = StringField('宠物名字', validators=[DataRequired(message='该项不能为空')], render_kw={"placeholder": "您的宠物名字"})
    age = IntegerField('宠物年龄', validators=[DataRequired(message='宠物年龄必须为正整数'), NumberRange(min=0)],render_kw={"placeholder": "您的宠物年龄"})
    breed = StringField('宠物品种', validators=[DataRequired(message='该项不能为空')], render_kw={"placeholder": "您的宠物品种"})
    submit = SubmitField('增加宠物')

class AddAppointment(FlaskForm):
    pet = SelectField('Your Pet',choices=[],validators=[DataRequired()])
    service = SelectField('Your Services',
                          choices=[('Emergency', "Emergency"), ('Standard','Standard')],
                          validators=[DataRequired()])
    city = SelectField('Your City',
                       choices=[('Beijing','Beijing'),('Shanghai','Shanghai'),('Chengdu','Chengdu')],
                       validators=[DataRequired()])
    symptom = StringField('symptom', validators=[DataRequired()],render_kw={"placeholder": "symptom"})
    submit = SubmitField('Add New Appointment')

class AddAppointment_ch(FlaskForm):
    pet = SelectField('您的宠物',choices=[],validators=[DataRequired()])
    service = SelectField('您的服务',
                          choices=[('Emergency', "紧急"), ('Standard','普通')],
                          validators=[DataRequired()])
    city = SelectField('您的城市',
                       choices=[('Beijing','北京'),('Shanghai','上海'),('Chengdu','成都')],
                       validators=[DataRequired()])
    symptom = StringField('宠物症状', validators=[DataRequired(message='该项不能为空')],render_kw={"placeholder": "症状"})
    submit = SubmitField('增加新的预约')

class MessageForm_ch(FlaskForm):
    subject = StringField('您的主题', validators=[DataRequired(message='该项不能为空')], render_kw={"placeholder": "我的提问主题 "})
    content = TextAreaField('您的内容', validators=[DataRequired(message='该项不能为空')], render_kw={"placeholder": "我的提问内容"})
    submit = SubmitField('提问')

class MessageForm(FlaskForm):
    subject = StringField('Your Subject', validators=[DataRequired()], render_kw={"placeholder": "Subject of My Post "})
    content = TextAreaField('Your Content', validators=[DataRequired()], render_kw={"placeholder": "Content of My Post"})
    submit = SubmitField('Make My Post')


class ChangeAppointmentState(FlaskForm):
    description = StringField('Description', validators=[DataRequired()], render_kw={"placeholder": "Input Your Description"})
    url = StringField('URL for your Video on Youtube', validators=[DataRequired()], render_kw={"placeholder": "Input Your Video URL"})
    submit = SubmitField('Change')

class ChangeAppointmentState_ch(FlaskForm):
    description = StringField('描述', validators=[DataRequired()], render_kw={"placeholder": "输入对宠物病情的描述"})
    url = StringField('您在Youtube上视频的URL', validators=[DataRequired()], render_kw={"placeholder": "输入您视频的URL"})
    submit = SubmitField('改变状态')

class ReplyForm(FlaskForm):
    content = TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Reply')

class ReplyForm_ch(FlaskForm):
    content = TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('回复')
