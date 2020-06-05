def sums(adds):
    def ass(*args,**kwargs):
        print("hello")
        return adds(*args,**kwargs)
    return ass

@sums
# @sums == add = sums(add)
def add():
    print(1 + 2)
@sums
def info(name, age):
    print(f"{name}{age}")
add()
info("fahis",12)