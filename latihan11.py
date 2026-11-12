# # membuat tuple
# data_tuples = (7, 8, 10, 11)
# print(data_tuples)

# # akses lewat indeks (mulai dari 0)
# print(data_tuples[1])
# print(data_tuples[-1])

# # # # boleh isi campur dan boleh ada duplikat
# # campur = ('budi', 20, 3.5, 20)
# # print(campur)

# # # # tuple satu elemen wajib pakai koma
# # satu = (5,)
# # bukan_tuple = (5)
# # print(type(satu))
# # print(type(bukan_tuple))

# # # data_tuples[1] = 'budi'
# # # data_tuples.append(1)
# # sementara = list(data_tuples)
# # sementara.append(1)
# # data_tuples = tuple(sementara)
# # print(data_tuples)

# # membuat set
# data_sets = {10, 4, 3, 2, 7, 6, 5}
# print(data_sets)

# # nilai kembar otomatis dihapus
# kembar = {10, 4, 3, 2, 2}
# print(kembar)

# # cek keanggotaan
# print(4 in data_sets)
# print(99 in data_sets)

# # set kosong
# kosong = set()
# print(type(kosong))
# print(type({}))

# # print(data_sets[0])
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a | b)   # gabungan (union)
# print(a & b)   # irisan (intersection)

# # menghilangkan duplikat dari list
# nilai = [10, 4, 3, 2, 4, 10]
# print(list(set(nilai)))

# list diakses dengan indeks
data_list = ['budi', 'rina', 'dimas']
print(data_list[0])

# dictionary diakses dengan key
data_dict = {
    'key': 'value',
    'bd': 'budi',
    'rn': 'rina',
    'dm': 'dimas',
    'umur': 20,
    'list': data_list
}
print(data_dict['bd'])
print(data_dict['umur'])
print(data_dict['list'])

data_dict = {
    'bd': 'budi santoso',
    'sr': 'sari wulandari',
    'dm': 'dimas pratama'
}

# panjang dictionary
print(f'panjang dictionary: {len(data_dict)}')

# cek key ada atau tidak
KEY = 'bd'
print(f'apakah {KEY} ada di data_dict: {KEY in data_dict}')

# membaca value
print(data_dict['bd'])
print(data_dict.get('bd'))
print(data_dict.get('xx', 'key tidak ditemukan'))

# mengubah dan menambah data
data_dict['bd'] = 'budi si rajin'
data_dict['tn'] = 'tono santoso'
data_dict.update({'bd': 'budi santoso'})
data_dict.update({'rn': 'rina maharani'})  # ditambah kalau key belum ada
print(data_dict)

# menghapus data
del data_dict['rn']
print(data_dict)

teman_teman = {
    'bd': 'budi santoso',
    'sr': 'sari wulandari',
    'dm': 'dimas pratama',
    'rn': 'rina maharani'
}

# loop biasa, yang keluar hanya key
for teman in teman_teman:
    print(teman)

# mengambil value
for value in teman_teman.values():
    print(value)

# mengambil key dan value sekaligus
for key, value in teman_teman.items():
    print(f'key = {key}, value = {value}')
