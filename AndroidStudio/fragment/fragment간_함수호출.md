1. 인터페이스 정의하기:
   먼저 Fragment에서 구현할 인터페이스를 정의합니다.

```
interface PotBottomSheetListener {
    fun onGetDetailRequested()
}
```

2. DetailFragment에 인터페이스 구현하기:
   다음으로 해당 인터페이스를 DetailFragment에서 구현합니다.

```
class DetailFragment : Fragment(), PotBottomSheetListener {
    // ...
    override fun onGetDetailRequested() {
        getDetail()
    }

    private fun getDetail() {
        // getDetail 함수 구현
    }
}
```

3. PotBottomSheet의 생성자를 변경하고 인터페이스 인스턴스 설정하기:
   PotBottomSheet 클래스의 생성자를 변경하여 PotBottomSheetListener 인스턴스를 전달받을 수 있도록 수정합니다.

```
class PotBottomSheet(context: Context, private val listener: PotBottomSheetListener) :
    BottomSheetDialogFragment() {

    // ...
}
```

4. DetailFragment에서 PotBottomSheet 인스턴스를 생성할 때 리스너 설정하기:
   이제 DetailFragment에서 PotBottomSheet 인스턴스를 생성할 때 리스너를 전달합니다.

```
val potBottomSheet = PotBottomSheet(requireContext(), this)
potBottomSheet.setPotId(potId)
potBottomSheet.show(
    mActivity.supportFragmentManager,
    potBottomSheet.tag
)
```

5. PotBottomSheet에서 인터페이스를 사용하여 함수 호출하기:
   이제 PotBottomSheet에서 인터페이스를 사용하여 DetailFragment의 함수를 호출할 수 있습니다.

```
class PotBottomSheet(context: Context, private val listener: PotBottomSheetListener) :
    BottomSheetDialogFragment() {

    // ...

    private fun someFunction() {
        listener.onGetDetailRequested()
    }
}
```

이제 PotBottomSheet에서 someFunction() 함수를 호출하면, DetailFragment의 getDetail() 함수가 실행됩니다. 이렇게 인터페이스를 사용하면 PotBottomSheet와 DetailFragment 간에 간단하게 통신할 수 있습니다.
