<script>
    export let type = 'submit';
    export let mode;
    export let disabled = false;
</script>
<style>
    button,
a {
  font-family: "Ubuntu";
  border: 1px solid #c9c9c9;
  background: #878787;
  padding: 0.5rem 1rem;
  color: white;
  border-radius: 5px;
  box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.26);
  cursor: pointer;
  text-decoration: none;
}

button:focus {
  outline: none;
}

button:hover,
button:active,
a:hover,
a:active {
  background: #257904;
  border-color: #067a10;
  box-shadow: 1px 1px 8px rgba(77, 51, 51, 0.26);
}

button:disabled,
button:disabled:hover,
button:disabled:active {
  background: #ccc;
  border-color: #ccc;
  color: #959595;
  box-shadow: none;
  cursor: not-allowed;
}

.success {
  background: var(--color--success--600);
  border-color: var(--color--success--700);
}

.success:hover,
.success:active {
  background: var(--color--success--500);
  border-color: var(--color--success--600);
}

.outline {
  background: transparent;
  color: var(--color--error--500);
  box-shadow: none;
}

.outline:hover,
.outline:active {
  background: #ffc7de;
  box-shadow: none;
}

.outline:disabled,
.outline:disabled:hover,
.outline:disabled:active {
  background: transparent;
  color: #ccc;
}

.outline.success {
  border-color: var(--color--success--300);
  color: var(--color--success--500);
}

.outline.success:hover,
.outline.success:active {
  background: #c2ffd1;
}

</style>

<button class= "{mode}" type="{type}" on:click {disabled}>
    <slot />
</button>
