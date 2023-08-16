package jpabook.jpashop.domain;

import javax.persistence.Embeddable;
import lombok.Getter;

@Embeddable // 내장타입
@Getter
public class Address {

    private String city;
    private String street;
    private String zipcode;

}
