# https://pywombat.com/my/exercises/4560e349

def sub_string(arr):
    assert len(arr) <= 5
    return arr[0] in arr[2] and arr[0] in arr[4] 

if __name__ == '__main__':
    #print(sub_string(['a', 'e', 'i', 'o']))
    print(sub_string(['a', 'e', 'i', 'o', 'u']))
    print(sub_string(['a', 'e', 'ia', 'o', 'ua']))
    print(sub_string(['o', 'a', 'hola', 'Eduardo', 'PyWombat']))
