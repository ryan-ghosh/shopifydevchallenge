
class repository:
    '''
    overarching repository class. will be implementing search and buy/sell methods. 
    '''
    def __init__(self):
        self.inventory = {} # key is image, item is stock
        self.capital = 0
    def __repr__(self):
        if self.inventory:
            for key in self.inventory:
                print("Picture: {}, stock: {}".format(key.gettag(), self.inventory[key]))
        else:
            print('Currently empty')

    def buy(self, item:str, price:float, descript:str):
        if self.capital-price<=0:
            print('Not sufficient funds')
            return
        for img in self.inventory:
            if img.gettag()==item:
                self.inventory[img] += 1
                self.capital -= price
                print('Congratulations on your new purchase!')
                return
        newimage = image(item, price, description=descript)
        self.inventory[newimage] = 1
        self.capital -= price
        print('Congratulations on your new purchase!')

    def sell(self, item:str, discount:float):
        for img in self.inventory:
            if img.gettag() == item:
                if self.inventory[img]>0:
                    self.inventory[img]-=1
                    self.capital += img.getprice() *(1-discount)
                    print('Enjoy your picture!')
                    return
                else:
                    print('Not currently in stock!')
        print('Not available')
                

    def search(self, description:str):
        for img in self.inventory:
            if description == img.gettag():
                return img
        dlist = description.split()
        images = []
        for word in dlist:
            for img in self.inventory:
                if word in img.description:
                    flag = 0
                    for item in images:
                        if item[0] == img.gettag():
                            item[1] -= 1
                            flag = 1
                    if not flag:
                        images.append([img.gettag(), -1])
        images.sort(key=lambda x:x[1])
        res = [i[0] for i in images]
        print('Possible images: {}'.format(res))




class image:
    def __init__(self, tag:str, price:float, description=None):
        self._tag = tag
        self._price = price
        self.description = set()
        if description:
            for word in description.split():
                self.description.add(word)
    def __repr__(self):
        return self._tag
    def getprice(self):
        return self._price
    
    def gettag(self):
        return self._tag
        
    def setprice(self, price):
        self._price = price
    
    def settag(self, tag):
        self._tag = tag
    
