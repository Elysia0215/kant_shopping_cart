from product import Product

class Cart:
    def __init__(self):
        # 빈 장바구니 생성
        self.items = {} # {상품:수량}
        
    def add(self, product, qty):
        # 품절 상품은 담을수 없다.
        if product.is_sold_out():
            print('품절된 상품입니다.')
            return
        
        # 이미 장바구니에 담겨있는 수량
        in_cart_qty= self.items.get(product,0) # 장바구니(items)있음 수량, 없으면 0
        # 더 담을 수 있는 수량 
        extra_qty = product.stock - in_cart_qty
        if qty > extra_qty: # 가능 재고 수량을 벗어남
            print(f'재고가 부족합니다. (담을 수 있는 수량:{extra_qty})')
            return
        
            
            
        
        # 처음이 아닌, 두번째에 담길떄 기존에 추가를 생각해야함.
        self.items[product] = self.items.get(product, 0) + qty #get (key값이 있음 key의 value 리턴, 없음 0, 그거에 + qty
        print(f'{product.name} {qty}개를 담았습니다.')
    
    # 장바구니에서 제거(빼기)
    def remove(self,product,qty):
        # 장바구니에 없는 상품은 뺄수 없음
        if product not in self.items:  # 어떤게 있냐 키워드 'in' # items = 장바구니
            print('장바구니에 해당 상품이 없습니다.')
            # in으로 쓰면 없는것도 처리 해야하니, 적은 사례 조건을 먼저 처리해서 빠져나가는게 더 나음
            return
        
        # 담은 수량 이상 빼면 상품을 통쨰 삭제
        ## 이러면 초과로 뺴는거에 대한 경고는 안나오긴함.
        if qty >= self.items[product]: #product = key
            del self.items[product] # 해당 상품을 딕셔너리에서 삭제
            print(f'{product.name}을 장바구니에서 모두 뺏습니다.')
        else:
            self.items[product] -= qty
            print(f'{product.name} {qty}개를 뺏습니다.')
    
    # 장바구니 비었는지 확인
    def is_empty(self):
        return len(self.items) ==0
    
    # 상품 합계 계산
    def subtotal(self):
        return sum( p.price * q for p,q in self.items.items())
    
    # 배송비 계산
    def shipping(self):
        if self.is_empty(): return 0 # 아예 장바구니가 비어있음 0
        return 0 if self.subtotal() >= 30_000 else 3_000 # 3만원 이상이면 return 0, 아니면 3_000
    # 결제 금액 계산
    def total(self):
        return self.subtotal() + self.shipping()
    
    # 장바구니 내용 출력
    def show(self):
        line = '-' * 40 # 반복 print('-'*40) 꼼수
        print(line)
        
        if self.is_empty():
            print('장바구니 비어 있습니다.')
            
        for p, q in self.items.items():
            # 제품명 x 가격 x 수량 = 금액
            print(f'{p.name:<10} x {q:<3} = {p.price * q:12,}원')      
        print(line)
        print(f"{'상품합계':<10} {self.subtotal():>15,}원")
        print(f"{'배송비':<10} {self.shipping():>15,}원")  
        print(f"{'결제 금액':<10} {self.total():>15,}원")
        print(line)
    def checkout(self):
        if self.is_empty():return
        
        self.show()
        # 재고 감소 처리
        for p,q in self.items.items():
            p.stock -= q # 장바구니에 담긴 수량 만큼 빼주기
        # 장바구니 비우기
        self.items.clear #clear dict을 깨끗하게 지우는 함수
        
        # 결제 성공여부 SKIP(Y/N)
        print('결제가 완료 되었습니다. 감사합니다.')
    
# ------------------------------------------------------------------
# 테스트 코드
# ------------------------------------------------------------------

# 제품 인스턴스 생성
tumbler = Product('텀블러',15_000,10)
earphone = Product('무선이어폰',89_000,3)

# 카트 인스턴스 생성
cart = Cart()

cart.show()
cart.add(tumbler, 1)
cart.show()
cart.add(earphone, 2)
cart.show()


print('남은 종류 : ', len(cart.items))





# for p,q in cart.items.items(): # 딕셔너리의 (상품 객체key, 수량)
#     # p: 상품 객체예요. 그래서 p.id, p.name처럼 속성에 접근할 수 있어요.
#     # q: 담은 수량이에요.
#     print(f' {p.id} : {p.name} x {q}')
    

