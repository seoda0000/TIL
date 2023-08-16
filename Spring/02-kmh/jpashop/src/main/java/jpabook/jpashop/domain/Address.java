package jpabook.jpashop.domain;

import javax.persistence.Embeddable;
import lombok.Getter;

@Embeddable // 내장타입
@Getter // 값 타입은 Setter 는 제공 X
public class Address {

    private String city;
    private String street;
    private String zipcode;

    // 엔티티나 임베디드 타입은 자바 기본 생성자를 public이나 protected로 설정해야 한다.
    protected Address() {

    }

    public Address(String city, String street, String zipcode) {
        this.city = city;
        this.street = street;
        this.zipcode = zipcode;
    }
}
