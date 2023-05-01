
import android.util.Log
import okhttp3.Interceptor
import okhttp3.OkHttpClient
import okhttp3.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitClient {
    private var retrofitClient: Retrofit? = null

    fun getClient(): Retrofit? {

        val client = OkHttpClient.Builder()

        var baseParameterInterceptor: Interceptor = (object : Interceptor {
            override fun intercept(chain: Interceptor.Chain): Response {
                val originalRequest = chain.request()
                val accessToken = GlobalVariables.prefs.getString(
                    "access_token",
                    ""
                ) // ViewModel에서 지정한 key로 JWT 토큰을 가져온다.

                Log.d("RetrofitClient", accessToken)
                val modifiedRequest = originalRequest.newBuilder()
                    .addHeader("content-type", "application/json")
                    .addHeader("Authorization", "Bearer $accessToken")
                    .build()

                val finalRequest = modifiedRequest.newBuilder()
                    .method(modifiedRequest.method, modifiedRequest.body)
                    .build()
                return chain.proceed(finalRequest)
            }

        })
        client.addInterceptor(baseParameterInterceptor)

        if (retrofitClient == null) {
            retrofitClient = Retrofit.Builder()
                .baseUrl(GlobalVariables.getBaseUrl())
                .addConverterFactory(GsonConverterFactory.create())
                .client(client.build())
                .build()
        }
        return retrofitClient
    }
}
