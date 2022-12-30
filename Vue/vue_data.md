# props, emit

- 부모-자식간 통신

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c3bef77d-35b1-4c0c-b517-718f78930fc0/Untitled.png)

```jsx
// 자식 요소에서 주기

export default {
  name: 'Child',
  methods: {
    toParent(event) {
      this.$emit('to-parent', event.target.value)
    }
  }
}

// 부모 요소에서 받기
<Child @to-parent="goParentEvent"></Child>
```

```jsx
// 부모 요소에서 주기
<Child :parent-data="parentData"></Child>

// 자식 요소에서 받기
export default {
  name: 'Child',
	props: {
    parentData: String
  },
}
```

---

# Vuex

- 데이터를 중앙에서 관리

## Component에서 데이터를 조작하기 위한 데이터 흐름

### `Component` → `(actions)` → `mutations` → `state`

- Actions

```jsx
// index.js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store',                    // 1. Component
  },
  mutations: {
    CHANGE_MESSAGE(state, newMessage) {             // 3. mutations
      state.message = newMessage                    // 4. state
    }
  },
  actions: {                                        // 2. actions
    changeMessage(context, newMessage) {
      context.commit('CHANGE_MESSAGE', newMessage)  // 3. mutations
    }
  },
  modules: {
  }
})
```

```html
// App.vue
<template>
  <div id="app">
    <h1>{{ message }}</h1>                               // 1. Component
    <input
      type="text"
      @keyup.enter="changeMessage"
      v-model="inputData"
    >
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      inputData: null,
    }
  },
  computed: {
    message() {                                           // 1. Component
      return this.$store.state.message
    },
  },
  methods: {
    changeMessage() {                                     // 2. actions
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
    }
  }
}
</script>

```

## Component에서 데이터를 사용하기 위한 데이터 흐름

### `state` → `(getters)` → `component`

```jsx
// index.js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {                                     // 1. state
    message: 'message in store',                 
  },
  getters: {
    messageLength(state) {                     // 2. getters
      return state.message.length
    },
    doubleLength(state, getters) {
      return getters.messageLength * 2         // 2. getters
    }
  },
  mutations: {
    CHANGE_MESSAGE(state, newMessage) {           
      state.message = newMessage
    }
  },
  actions: {                                    
    changeMessage(context, newMessage) {
      context.commit('CHANGE_MESSAGE', newMessage) 
    }
  }
})
```

```html
// App.vue
<template>
  <div id="app">
    <h1>{{ message }}</h1>                    
    <h2>입력된 문자의 길이는 {{ messageLength }}</h2>   // 3. Components
    <h2>두배하면 {{ doubleLength }}</h2>               // 3. Components
    <input
      type="text"
      @keyup.enter="changeMessage"
      v-model="inputData"
    >
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      inputData: null,

    }
  },
  components: {
  },
  computed: {
    message() {                                        
      return this.$store.state.message
    },
    messageLength() {                                   
      return this.$store.getters.messageLength        // 3. Components
    },
    doubleLength() {
      return this.$store.getters.doubleLength         // 3. Components
    } 
  },
  methods: {
    changeMessage() {                      
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
    }
  }
}
</script>

```

---

# EventBus

- 비부모-자식

![Untiaaaatled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6fc6c3b9-c11a-4b2d-99c8-5f41947a5cda/Untiaaaatled.png)

- 이벤트의 중앙 매개체
- 공통으로 데이터들을 주고 받을 수 있는 공간

```jsx
//EventBus.js
import Vue from 'vue';
export default new Vue();
```

## $emit : 이벤트 보내기

- EventBus에 emit으로 이벤트를 보낸다.

### `EventBus.$emit(이벤트 이름, 보낼 값)`

```jsx
// 보내는 컴포넌트
import EventBus from './EventBus'
export default {
    name: 'sender-app',
    data () {
        return {
            text: '',
        }
    },
    methods: {
        send() {
            EventBus.$emit('message', this.text);
            this.text = '';
        },
    }
}
```

## **$on : 이벤트 구독하기**

- 컴포넌트에서 사용할 EventBus를 created에 등록해준다.

### `EventBus.$on('이벤트', this.컴포넌트메서드(이벤트핸들러));`

```jsx
//받는 컴포넌트
import EventBus from './EventBus'
export default {
    name: 'receiver-app',
    data () {
        return {
            receiveList: []
        }
    },
    created() {
        EventBus.$on('message', this.receive);
    },
    methods: {
        receive(text) {
            this.receiveList.push(text);
        }
    }
}
```