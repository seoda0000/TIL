```java
@SpringBootTest
@AutoConfigureMockMvc
@TestPropertySource(locations = "classpath:/application-local-db.properties")
@Transactional
class Test {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private WebApplicationContext wac;

    @PersistenceContext
    private EntityManager em;

    // 한글 깨짐 방지
    @BeforeEach
    public void setup() {
        this.mockMvc = MockMvcBuilders.webAppContextSetup(wac)
            .addFilters(new CharacterEncodingFilter("UTF-8", true))
            .alwaysDo(print())
            .build();
    }
}
```
