<template>
<div>
  <v-app-bar-nav-icon @click.stop="drawer = !drawer"
  x-large
  class="nav-icon"></v-app-bar-nav-icon>
  <v-navigation-drawer
    v-model="drawer"
    absolute
    bottom
    temporary
  >
    <v-list
      nav
      dense
    >
      <v-list-item-group
        class="menu-list"
        v-model="group"
        active-class="deep-purple--text text--accent-4"
      >


        <v-list-item>
          <v-list-item-icon>
            <v-icon color="#FF3D00">mdi-filmstrip</v-icon>
          </v-list-item-icon>
          <v-list-item-title><router-link class="text-decoration-none" style="display: block;" :to="{ name: 'main' }">영화</router-link></v-list-item-title>
        </v-list-item>

        <v-list-item>
          <v-list-item-icon>
            <v-icon color="#FF3D00">mdi-text-box-edit-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-title><router-link class="text-decoration-none" style="display: block;" :to="{ name: 'community' }">게시판</router-link></v-list-item-title>
        </v-list-item>

        <v-list-item v-if="!isLoggedIn">
          <v-list-item-icon>
            <v-icon color="#FF3D00">mdi-account-arrow-right-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-title><router-link class="text-decoration-none" style="display: block;" :to="{ name: 'login' }" >로그인</router-link></v-list-item-title>
        </v-list-item>

        <v-list-item v-if="!isLoggedIn">
          <v-list-item-icon>
            <v-icon color="#FF3D00">mdi-account-plus-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-title><router-link class="text-decoration-none" style="display: block;" :to="{ name: 'signup' }" >회원가입</router-link></v-list-item-title>
        </v-list-item>

        <v-list-item v-if="isLoggedIn">
          <v-list-item-icon>
            <v-icon color="#FF3D00">mdi-account-circle-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-title><router-link class="text-decoration-none" style="display: block;" :to="{ name: 'profile', params: {userId: currentUser.pk } }" >내 정보</router-link></v-list-item-title>
        </v-list-item>
        
        <v-list-item v-if="isLoggedIn">
          <v-list-item-icon>
            <v-icon color="#FF3D00">mdi-account-arrow-left-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-title><router-link class="text-decoration-none" style="display: block;" :to="{ name: 'logout' }" >로그아웃</router-link></v-list-item-title>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-navigation-drawer>
</div>
<!-- <div>

<v-app-bar
  absolute
  color="white"
  elevate-on-scroll
  scroll-target="#scrolling-techniques-7"
>
  <v-app-bar-nav-icon></v-app-bar-nav-icon>

  <v-toolbar-title>Title</v-toolbar-title>

  <v-spacer></v-spacer>

  <v-btn icon>
    <v-icon>mdi-magnify</v-icon>
  </v-btn>

  <v-btn icon>
    <v-icon>mdi-heart</v-icon>
  </v-btn>

  <v-btn icon>
    <v-icon>mdi-dots-vertical</v-icon>
  </v-btn>
</v-app-bar>
<v-sheet
  id="scrolling-techniques-7"
  class="overflow-y-auto"
  max-height="600"
>
  <v-container style="height: 1500px;">
  </v-container>
</v-sheet>
</div> -->
  <!-- <div>

    <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#Menu" aria-controls="Menu">
      메뉴
    </button>


    <div class="offcanvas offcanvas-start" tabindex="-1" id="Menu" aria-labelledby="MenuLabel">
      <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="MenuLabel">메뉴</h5>
        <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div class="offcanvas-body">
        <div>
          <p><router-link :to="{ name: 'main' }">영화</router-link></p>
          <p><router-link :to="{ name: 'community' }">게시판</router-link></p>
          <p><router-link :to="{ name: 'login' }" v-if="!isLoggedIn">로그인</router-link></p>
          <p><router-link :to="{ name: 'signup' }" v-if="!isLoggedIn">회원가입</router-link></p>
          <p><router-link :to="{ name: 'profile' }" v-if="isLoggedIn">내 정보</router-link></p>
          <p><router-link :to="{ name: 'logout' }" v-if="isLoggedIn">로그아웃</router-link></p>
        </div>
      </div>
    </div>
  </div> -->

</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'MenuList',
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser'])
  },
  data: () => ({
      drawer: false,
      group: null,
    }),

  watch: {
    group () {
      this.drawer = false
    },
  },
}
</script>

<style>
  .menu-list * {
    color: black;
    font-size: 1rem;
  }
</style>