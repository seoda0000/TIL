package com.example.stockapp;

import static android.content.Context.MODE_PRIVATE;

import android.content.Context;
import android.content.SharedPreferences;
import android.preference.Preference;
import android.preference.PreferenceManager;
import android.util.Log;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Response;
import com.android.volley.toolbox.StringRequest;

import java.util.HashMap;
import java.util.Map;

public class LoginRequest extends StringRequest {
    Context context;
    private SharedPreferences pref;

    // 서버 URL 설정
    final static private String URL = "http://13.124.21.50:8080/api/user/login";
    private Map<String, String> map;

    public LoginRequest(String userID, String userPass, Response.Listener<String> listener) {
        super(Method.POST, URL, listener, null);

        map = new HashMap<>();
        map.put("id", userID);
        map.put("password", userPass);
    }

    @Override
    protected Map<String, String> getParams() throws AuthFailureError {
        return map;
    }


    // 세션 정보 가져오기

    @Override
    protected Response<String> parseNetworkResponse(NetworkResponse response) {
        Map<String, String> responseHeaders = response.headers;
        String cookies = responseHeaders.get("Set-Cookie");

        String sessionid = cookies.split(";\\s*")[0];
        Log.e("hahaha", sessionid);
        setSessionIdInSharedPref(sessionid);




        return super.parseNetworkResponse(response);
    }


    private void setSessionIdInSharedPref(String sessionid){
        context = LoginActivity.context;
        Log.d("hahaha", "시도중");
        pref = context.getSharedPreferences("sessionCookie", Context.MODE_PRIVATE);
        Log.d("hahaha", "시도중..");
        SharedPreferences.Editor edit = pref.edit();
        Log.d("hahaha", "시도중....");
        if(pref.getString("sessionid",null) == null){ //처음 로그인하여 세션아이디를 받은 경우
            Log.d("hahaha","처음 로그인하여 세션 아이디를 pref에 넣었습니다."+sessionid);
        }else if(!pref.getString("sessionid",null).equals(sessionid)){ //서버의 세션 아이디 만료 후 갱신된 아이디가 수신된경우
            Log.d("hahaha","기존의 세션 아이디"+pref.getString("sessionid",null)+"가 만료 되어서 "
                    +"서버의 세션 아이디 "+sessionid+" 로 교체 되었습니다.");
        }
        edit.putString("sessionid", sessionid);
        Log.d("hahaha", "시도중 .....................");
        edit.apply(); //비동기 처리
    }

}
