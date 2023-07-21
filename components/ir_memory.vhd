library ieee; -- importing ieee library
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity ir_memory is
    port(
        -- PC input
        pc_input: in std_logic_vector(15 downto 0);

        -- IR output
        ir      : out std_logic_vector(15 downto 0) 
    );
end entity ir_memory;

architecture working of ir_memory is
    
    type ir_array is array (0 to (2**16)-1 ) of std_logic_vector (15 downto 0);
signal ir_mem : ir_array:=( b"0011001000000011", b"0011010000000011", b"0011011000000100", b"0011100000001000", b"0011101000000010", b"0011110000001011", b"0011111000000011", b"0001001100100000", b"0000010010000111", b"0001011011010000", b"0010100001001000", b"0001010001011000", b"0001010011001010",  others => x"EFFF" );
																																																																																																																																								    
begin

    ir_update_process:process(pc_input)
    begin
        ir <= ir_mem(to_integer(unsigned(pc_input)));
    end process ir_update_process;

end architecture working;