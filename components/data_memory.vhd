library ieee; -- importing ieee library
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity data_memory is
    port(
        -- reading memory data
        read_addr : in std_logic_vector(15 downto 0);
        read_data : out std_logic_vector(15 downto 0);

        -- writting memory data 
        write_addr : in std_logic_vector(15 downto 0);
        write_data : in std_logic_vector(15 downto 0);

        -- write enable
        write_en    : in std_logic;
        -- Clock 
        clock  : in std_logic -- clock
    );
end entity data_memory;

architecture working of data_memory is
    
    type data_array is array (0 to (2**16)-1) of std_logic_vector (15 downto 0);
    signal data_mem : data_array:=(
        x"0000",x"0001", x"0002", x"0003",
        x"0004",x"0005", x"0006", x"0007",
        x"0008",x"0009", x"000A", x"000B",
        x"000C",x"000D", x"000E", x"000F",
        x"00F1",x"00F2", x"00F3", x"00F4",
        x"00F5",x"00F6", x"00F7", x"00F8",
        x"00F9",x"00FA", x"00FB", x"00FC",
        x"00FD",x"00FE", x"00FF", x"0FF1", others => x"0000"); 
     
begin
    
    -- reading data from mem_data
    data_read:process(read_addr)
    begin
        read_data <= data_mem(to_integer(unsigned(read_addr)));
    end process;

    -- writting data to mem_data
    data_write:process(clock)
    begin
        if(falling_edge(clock)) then
            if(write_en = '1') then
                data_mem(to_integer(unsigned(write_addr))) <= write_data;
            end if;
        end if;
    end process;
    
end architecture working;