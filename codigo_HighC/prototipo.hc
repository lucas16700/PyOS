#import <io>
// ================================================
// Exemplo de codigo de HighC
// ================================================

high config = {
    resolution: [1920, 1080],
    title:      "Meu Projeto",
    vsync:      true,
    max_fps:    144
}

high player = {
    position: [100, 200],
    speed:    5.5,
    inventory: ["sword", "potion", "key"]
}

data nome = "hello world"

fn main() {
    window := gfx.Window(config.resolution, title: config.title)
    
    while window.is_open() {
        window.clear(0.1, 0.1, 0.15)
        
        if keyboard.pressed('SPACE') {
            spawn_particle(player.position)
        }
        
        update_game()
        render_game()
        
        window.flip()
    }
    
    print("Programa finalizado.")
}

// Função com tipo explícito (estilo mais C)
fn update_game() -> void {
    player.position[0] += player.speed
}

// Função nativa / baixo nível (opcional)
@[native]
fn render_game() {
    // Aqui ainda esta sendo desenvolvido
}