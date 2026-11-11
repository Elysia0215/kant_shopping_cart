class Product:
    # 클래스 변수 선언
    next_id = 1 # 모든 상품들이 공유하는 번호
    
    # 새 상품의 초기 정보 저장
    def __init__(self, name, price, stock):
        self.id = Product.next_id
        Product.next_id += 1 # 다음 상품을 위해 Index 값 +1
        
        self.name = name
        self.price = price
        self.stock = stock
        
    def is_sold_out(self): # 변수 앞에 is 붙으면 보통 불린값 , 보통 긍정으로 변환해야 함, True로 쓸 수 있도록
        return self.stock == 0     
    
    def __str__(self):
        stock_text ='품절' if self.is_sold_out() else f'재고 {self.stock}개'
        return f'{self.id} {self.name:<10} {self.price:>8,} {stock_text}'

# ------------------------------------------------------------------
# 테스트 코드
# ------------------------------------------------------------------

if __name__ == "__main__":
    products = [
        Product('무선 이어폰', 80_000, 3),
        Product('텀플러', 30_000, 10),
        Product('보조 배터리', 32_000, 10),
        Product('마우스패드', 9_000, 10),
        Product('USB 허브', 30_000, 10),
    ]        

    # 출력코드 - import하면 파일에 있는 실행코드를 실행 시킴,
    # 안할려면 if __name__ = '__main__' 조건을 걸어야함.
    # name이 시작점이 어디냐. 
    for p in products: print(p)


