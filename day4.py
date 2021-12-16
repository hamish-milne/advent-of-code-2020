passports = [{f[0]:f[1] for f in (fs.split(':') for line in p.splitlines() for fs in line.split(' ')) } for p in open('day4.txt').read().split('\n\n')]
keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
print(sum(1 if all(key in passport for key in keys) else 0 for passport in passports))
