<script></script>

<template>
  <nav>
    <div class="nav-container">
      <div class="logo">
        <span>R<span style="color: tomato">@</span>MIMS</span>
      </div>
      <ul>
        <li><a href="">Home</a></li>
        <li><a href="">About Us</a></li>
        <li><a href="">Gallery</a></li>
        <li><a href="">Blog</a></li>
        <div class="banner">Get in Touch</div>
      </ul>
    </div>
  </nav>

  <header>
    <h1>Mummy Rach Metamorphosis Center</h1>
    <span class="action-statement">You get what you deserve</span>
    <button>Contact Us</button>
  </header>
  <main>
    <section id="offers">
      <div class="service-box">
        <div class="service-header">
          <!-- Image title here -->
          <h5>Service 1</h5>
        </div>
      </div>
      <div class="service-box">
        <div class="service-header">
          <!-- Image title here -->
          <h5>Service 2</h5>
        </div>
      </div>

      <div class="service-box">
        <div class="service-header">
          <!-- Image title here -->
          <h5>Service 3</h5>
        </div>
      </div>

      <div class="service-box">
        <div class="service-header">
          <!-- Image title here -->
          <h5>Service 4</h5>
        </div>
      </div>
    </section>
    <section id="customer-section">
      <div class="left-side">
        <h3>What makes us a customer favorite</h3>
        <div class="left-side-body">
          <div class="image-header">
            <img src="" alt="some image" />
          </div>
          <p>Yes there is some content here</p>
        </div>
        <div class="left-side-body">
          <div class="image-header">
            <img src="" alt="some image" />
          </div>
          <p>Yes there is some content here</p>
        </div>
        <div class="left-side-body">
          <div class="image-header">
            <img src="" alt="some image" />
          </div>
          <p>Yes there is some content here</p>
        </div>
      </div>

      <div class="right-side">
        <form action="">
          <input type="text" placeholder="Name" />
          <input type="text" placeholder="Phone Number" />
          <textarea name="message" id=""></textarea>
          <button class="">Contact Us</button>
        </form>
      </div>
    </section>
    <section id="gallery">
      <h1>Gallery</h1>
      <div class="image-container">
        <img src="" alt="" />
        <img src="" alt="" />
        <img src="" alt="" />
        <img src="" alt="" />
      </div>

      <button class="">More Pictures</button>
    </section>
  </main>
  <footer>
    <p>Build by Venom</p>
  </footer>
</template>

<style scoped>
/*
NAVBAR SECTION
*/

nav {
  width: 100%;
  height: 100vh;
  background-image: url("../assets/images/home.jpeg");
}

.nav-container {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  padding: 3% 7%;
}

.nav-container ul {
  list-style: none;
  display: flex;
  flex-direction: row;
  font-size: 20px;
}

.nav-container ul li {
  margin-left: 15px;
  margin-right: 15px;
  padding: 7px;
}

.nav-container ul li:hover {
  background-color: greenyellow;
}

.nav-container a {
  text-decoration: none;
  color: white;
}

.logo {
  height: inherit;
  font-weight: bold;
  font-size: 30px;
  cursor: pointer;
}

.banner {
  align-self: center;
  margin-left: 20px;
  background-color: purple;
  font-weight: bold;
  border-radius: 10px;
  padding: 5px;
}
</style>
