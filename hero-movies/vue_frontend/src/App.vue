<template>
  <div id="app">
    <div class="p-4 d-flex">
      <menu-list class="d-flex"></menu-list>
      <h1 class="main-title">영웅, 영화들</h1>
    </div>
    <router-view/>
    <v-btn
      class="up-btn mx-2"
      fab
      dark
      small
      color="#2962FF"
      @click="onUp"
    >
      <v-icon dark>
        mdi-chevron-up
      </v-icon>
    </v-btn>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList.vue'
import { mapActions } from 'vuex'

export default {
  name: 'App',
  components: {
    MenuList,
  },
  methods: {
    ...mapActions(['fetchCurrentUser']),
    onUp() {
      window.scrollTo(0, 0)
    }
  },
  created() {
    this.fetchCurrentUser()
  }
}
</script>
<style>
  body {
    max-width: 1000px !important;
    margin: auto !important;
    background-image: url('../spy.jpg');
    background-size: 50%;
    background-position: 100% 0;
  }
  .up-btn {
    position: fixed;
    right: 20px;
    bottom: 20px;
  }
  .main-title {
    margin-left: 35%;
  }

</style>
