import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { Quasar } from 'quasar'
import langZh from 'quasar/lang/zh-CN'
import { createI18n } from 'vue-i18n'
import zh from './locales/zh-CN.json'

// Import icon libraries
import '@quasar/extras/material-icons/material-icons.css'

// Import Quasar css
import 'quasar/src/css/index.sass'


import App from './App.vue'
import router from './router'

const i18n = createI18n({
  locale: 'zh-CN',
  messages: {
    'zh-CN': zh,
  },
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(Quasar, {
  lang: langZh,
  plugins: {}, // import Quasar plugins and add here
})
app.use(i18n)

app.mount('#app')
