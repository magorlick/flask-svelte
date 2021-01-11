<script>
    import { onMount } from 'svelte';
    export let name;
    
    import routes from "./routes/routes.js";
    import page from "page";

    let currentPage = routes.rand;

    function setPage({ params: { page, view } }) {
        currentPage = routes[page];
        console.log('setPage', currentPage)
    }

    function updateAfterMoving(ctx) {
        ctx.path += `?currentQuery`;
        ctx.save();
    }
    page("/", () => setPage({ params: { page: 'rand', view: 'test' } }), updateAfterMoving);
    page("/rand", () => setPage({ params: { page: 'rand', view: 'test' } }), updateAfterMoving);
    page("/:page/:view", setPage);
    page({ hashbang: true });

    function addInput(event) {
        console.log('addInput', event.detail.numberInput);
    }
    
    function updateQueryString(query) {
        if (window.history.replaceState) {
            let hash = window.location.hash.split('?')[0];
        if (hash.length === 0 || hash === '#!/') {
            hash = '';
        }
        const newURL = `${window.location.origin}${window.location.pathname}${hash}?${query}`
        window.history.replaceState(null, null, newURL);
        }
    }

    let mounted = false;
    onMount(() => { mounted = true });

    // $: if (mounted) updateQueryString('');
    
</script>

<style>
    .right-menu {
        display: flex;
        flex-flow: row wrap;
        justify-content: flex-end;
    }

    .center-menu {
        display: flex;
        flex-flow: row wrap;
        justify-content: space-around;
    }

    .wrapper {
        display: flex;  
        flex-flow: row wrap;
        font-weight: bold;
        text-align: left;
        align-content: flex-end
    }

    .wrapper > * {
        padding: 10px;
        flex: 1 100%;
    }

    @media all and (min-width: 600px) {
    .aside { flex: 1 0 0; }
    }
</style>

<div class = "app">
    <header>
        <div class="wrapper">
            <aside class="aside aside-3">
              <h1>
                Flask + Svelte:
                <span>A data science web app.</span>
              </h1>
            </aside>
          </div>
    </header>
    <main>
        <h1> Hello {name}!</h1>
        <svelte:component this={currentPage.body} params={currentPage.params} on:inputForm="{addInput}" />

    </main>
</div>