passports = [{f[0]:f[1] for f in (fs.split(':') for line in p.splitlines() for fs in line.split(' ')) } for p in open('day4.txt').read().split('\n\n')]
def num(s: str, a: int, b: int):
    if s.isdigit():
        i = int(s)
        return i >= a and i <= b
    return False
def byr(s: str):
    return num(s, 1920, 2002)
def iyr(s: str):
    return num(s, 2010, 2020)
def eyr(s: str):
    return num(s, 2020, 2030)
def hgt(s: str):
    if s.endswith('cm'):
        return num(s[:-2], 150, 193)
    if s.endswith('in'):
        return num(s[:-2], 59, 76)
    return False
def hcl(s: str):
    if s.startswith('#') and len(s) == 7:
        return all(c.isdigit() or ord(c) in range(ord('a'),ord('f')+1) for c in s[1:])
    return False
def ecl(s: str):
    return s in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
def pid(s: str):
    return len(s) == 9 and s.isdigit()
valids = {
    'byr':byr,
    'iyr':iyr,
    'eyr':eyr,
    'hgt':hgt,
    'hcl':hcl,
    'ecl':ecl,
    'pid':pid
}
print(sum(1 if all(key in passport and valids[key](passport[key]) for key in valids) else 0 for passport in passports))
