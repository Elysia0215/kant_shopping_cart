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
    
# ------------------------------------------------------------------
# 테스트 코드
# ------------------------------------------------------------------

# 제품 인스턴스 생성
tumbler = Product('텀블러',15_000,10)
mousepad = Product('마우스 패드',9_000,0)

# 카트 인스턴스 생성
cart = Cart()
cart.add(tumbler, 10)
cart.remove(tumbler, 3)
cart.remove(mousepad, 1)
cart.remove(tumbler, 8) # 현재 재고 7 < 8 => 전체 삭제

print('남은 종류 : ', len(cart.items))





# for p,q in cart.items.items(): # 딕셔너리의 (상품 객체key, 수량)
#     # p: 상품 객체예요. 그래서 p.id, p.name처럼 속성에 접근할 수 있어요.
#     # q: 담은 수량이에요.
#     print(f' {p.id} : {p.name} x {q}')
    

