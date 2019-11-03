class Test:
    list = [1, 2, 8, 4, 6, 7]
    tup = (100, 200)
    dic1 = {'one': 1, 'two': 2, 3: 'three'}

    def test(self):
        print('Test');

    def iterate_list(self):
        for item in self.list:
            print(item)

    def iterate_list_in_reverse(self):
        new_list = reversed(self.list)
        return new_list

    def add_new_item_in_list(self, item):
        self.list.append(item)
        # print(self.list)

    def remove_item_from_list(self, item):
        self.list.remove(item)

    def search_in_dictionary(self, item):
        return self.dic1.get(item)

    def iterate_dic(self):
        print(self.dic1)
        for item1 in self.dic1:
            print('item in dic: {}'.format(item1))

    def work_on_tuple(self):
        pass

    def work_on_set(self):
        pass

    def work_on_list(self):
        pass


test = Test()
print(test.tup)
item = test.search_in_dictionary('two')
dic2 = test.dic1.copy()
print('##### {}'.format(test.dic1.pop('one')))
# print('##### {}'.format(dic2.popitem()))
# print('##### {}'.format(dic2.popitem()))
print(dic2.__len__())
test.iterate_dic()
print('dic1 = {}'.format(test.dic1))
print('dic2 = {}'.format(dic2))
tup1 = test.tup.__hash__()
print(int(tup1))
dic2.update({'five': 5, 'one': 27})
print(dic2)
dic2.__delitem__(3)
print('dic2 after delete of key 3: {}'.format(dic2))
print('len of dic2: {}'.format(dic2.__len__()))
test.list.sort(reverse=True)
print(test.list)
dic2.update({'one': 8})
print(test.tup.__sizeof__())

set = set()
set.add(22)
set.add(33)
set.add(44)
set.add(55)
contains = set.__contains__(38)
print('size of set {c} # {dic}'.format(c=contains, dic=dic2))
try:
    tp = test.tup.count(100); print(f'tuple {tp}');

except TypeError:
    print('wrong method used')

# try:
#     test.search_in_dictionary(2)
# except:
#     print("item not found in dictionary")



# test.iterate_list()
# test.iterate_list_in_reverse()
# print(test.list)
# copy_list = test.tup.__contains__(2)
# test.add_new_item_in_list(200)
# test.add_new_item_in_list(300)
# test.add_new_item_in_list(200)
# test.add_new_item_in_list(200)
# test.add_new_item_in_list(400)
# copy_list.append(111)
# print(test.list)
# print('type of copy_list {}'.format(type(copy_list)))
# print(list.index())
# try:
#     test.remove_item_from_list(200)
# except:
#     print('item not found in list')
# test.remove_item_from_list(200)
# print(test.list)
# copy_list = test.list.copy()
# print(copy_list)


