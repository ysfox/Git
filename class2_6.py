names = ['Michael','Bob','Tracy'];
scores = [95,75,85];

d = {'Michael':95,'Bob':75,'Tracy':85};
print(d['Michael']);

d['Adam'] = 65;
print(d['Adam'];

d['Jack'] = 90;
print(d['Jack']);
d['Jack'] = 88;
print(d['Jack']);

print('Thomas' in d);

print(d.get('Thomas'));
print(d.get('Thomas'),-1);

d.pop('Bob');
print(d);

s = set([1,2,3]);
print(s);
