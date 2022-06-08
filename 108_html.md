[data-testid=username] usar especificar

```html
        <div class="form-group">
          <label for="inputEmail">Usuário</label>
          <input
            id="inputEmail"
            v-model="user.username"
            type="text"
            class="form-control"
            placeholder="SEU USUÁRIO"
            data-testid="username"
            required
            autofocus
          />
        </div>

        <div class="form-group">
          <label for="inputPassword">Senha</label>
          <input
            id="inputPassword"
            v-model="user.password"
            type="password"
            class="form-control"
            data-testid="password"
            placeholder="***"
            required
          />
```