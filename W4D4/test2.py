class Car:
    def __init__(self):
        print("초기화")
    def __del__(self):
        print("소멸자 호출: 더이상 이 객체를 안써서 인스턴스 삭제함")
    #문자열화 해 반환
    def __str__(self):
        return "str 메소드가 호출됨"


'''
매직함수 : 가장 일반적인 용도 : 오퍼레이터 오버로딩용으로 가장 자주 쓰임
+   def __add__
-   def __sub__
*   def __mul__
/   def __truediv__
//  def __floordiv__
%   def __mod__
**  def __pow__
<   def __lt__
>   def __gt__
>=  def __ge__
<=  def __le__

'''