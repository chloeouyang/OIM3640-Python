def check_fermat(a,b,c,n):
    """check to see if Fermat's theorem holds"""
    if n>2 and a**n+b**n=c**n:
        print('Holy smokes,Fermat was wrong!')
    else:
        print('No, that doesn\'t work')