guests = ['Ningguang', 'Hutao', 'Xiao', 'Childe']
behaviors = {
   'Ningguang': 'memeriksa kue',
   'Hutao': 'memberikan kado tanpa memperhatikan kue',
   'Xiao': 'memotret apa pun yang dia lihat pertama kali di ruangan',
   'Childe': 'membawa air mineral dan meletakkannya di meja sebelum memberikan kado'
}
fact = "Foto Xiao menunjukkan kue masih utuh di meja"
difoto_utuh = True
if difoto_utuh:
    print('Individu yang paling mungkin mencuri kue: Childe')
else:
    print('Individu yang paling mungkin mencuri kue: Ningguang atau Hutao')