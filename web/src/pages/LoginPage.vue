<template>
  <div class="q-pa-md" style="max-width: 400px">
    <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
      <q-input
        filled
        v-model="username"
        label="User name *"
        hint="User name"
        lazy-rules
        :rules="[(val) => (val && val.length > 0) || 'Please input username']"
      />
      <q-input
        filled
        v-model="password"
        label="Password *"
        hint="Password"
        :type="isPwd ? 'password' : 'text'"
        lazy-rules
        :rules="[(val) => (val && val.length > 0) || 'Please input password']"
      >
        <template v-slot:append>
          <q-icon
            :name="isPwd ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd = !isPwd"
          />
        </template>
      </q-input>

      <div>
        <q-btn label="login" type="submit" color="primary" />
      </div>
    </q-form>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue'
import { ajax } from '../utils/request'
import { storage } from '../stores/storage'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')

const isPwd = ref(true)

const router = useRouter()
const onReset = () => {
  username.value = ''
  password.value = ''
}
const onSubmit = async () => {
  const formData = new FormData()
  formData.append('username', username.value)
  formData.append('password', password.value)
  await ajax.post('/token/', formData).then(async (res) => {
    const access_token = res.data.access_token
    storage.setItem('token', access_token)
    storage.setItem('username', username.value)
    await router.push('/')
  })
}
</script>
