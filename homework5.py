immutable_=('way',73,True,[4,8,15])
print(immutable_)
#immutable_.append('Samurai')# потому что создатель языка хотел иметь тип данных, которые не поддаются изменениям  и незыблимы, как китайская стена или государственные кортежи.
immutable_[3][1]=14
mutable_list=['women',7, False]
print(mutable_list)
mutable_list.extend('children')
print(mutable_list)